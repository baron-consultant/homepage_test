const DEFAULT_DOCUMENT = 'index.html';
const DEFAULT_CONTENT_TYPE = 'application/octet-stream';

export default {
  async fetch(request, env) {
    if (!env.SITE_BUCKET) {
      return new Response('R2 bucket binding SITE_BUCKET is missing.', { status: 500 });
    }

    if (request.method !== 'GET' && request.method !== 'HEAD') {
      return new Response('Method Not Allowed', {
        status: 405,
        headers: { Allow: 'GET, HEAD' },
      });
    }

    const url = new URL(request.url);
    const keyCandidates = buildKeyCandidates(url.pathname);

    for (const key of keyCandidates) {
      const object = await env.SITE_BUCKET.get(key);
      if (!object) {
        continue;
      }

      return createObjectResponse(object, key, request.method === 'HEAD');
    }

    return new Response('Not Found', {
      status: 404,
      headers: {
        'content-type': 'text/plain; charset=utf-8',
        'cache-control': 'no-store',
      },
    });
  },
};

function buildKeyCandidates(pathname) {
  const normalizedPath = normalizePath(pathname);

  if (!normalizedPath) {
    return [DEFAULT_DOCUMENT];
  }

  const candidates = [normalizedPath];

  if (normalizedPath.endsWith('/')) {
    candidates.unshift(`${normalizedPath}${DEFAULT_DOCUMENT}`);
  } else if (!hasFileExtension(normalizedPath)) {
    candidates.push(`${normalizedPath}/${DEFAULT_DOCUMENT}`);
  }

  return Array.from(new Set(candidates));
}

function normalizePath(pathname) {
  let normalized = pathname || '/';

  try {
    normalized = decodeURIComponent(normalized);
  } catch {
    return '';
  }

  if (normalized === '/' || normalized === '') {
    return '';
  }

  normalized = normalized.replace(/^\/+/, '');
  normalized = normalized.replace(/\/+/g, '/');

  const segments = normalized.split('/').filter(Boolean);
  if (segments.some((segment) => segment === '.' || segment === '..')) {
    return '';
  }

  const rebuilt = segments.join('/');
  if (pathname.endsWith('/')) {
    return rebuilt ? `${rebuilt}/` : '';
  }

  return rebuilt;
}

function hasFileExtension(pathname) {
  const lastSegment = pathname.split('/').pop() || '';
  return lastSegment.includes('.');
}

function createObjectResponse(object, key, headOnly) {
  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set('etag', object.httpEtag);

  if (!headers.has('content-type')) {
    headers.set('content-type', inferContentType(key));
  }

  if (!headers.has('cache-control')) {
    headers.set('cache-control', inferCacheControl(key));
  }

  if (headOnly) {
    return new Response(null, { status: 200, headers });
  }

  return new Response(object.body, { status: 200, headers });
}

function inferCacheControl(key) {
  const extension = (key.split('.').pop() || '').toLowerCase();

  switch (extension) {
    case 'html':
      return 'no-cache, no-store, must-revalidate';
    case 'css':
    case 'js':
    case 'mjs':
    case 'json':
    case 'svg':
    case 'png':
    case 'jpg':
    case 'jpeg':
    case 'gif':
    case 'webp':
    case 'ico':
    case 'woff':
    case 'woff2':
    case 'ttf':
    case 'otf':
    case 'mp4':
    case 'webm':
    case 'pdf':
      return 'public, max-age=31536000, immutable';
    default:
      return 'public, max-age=3600';
  }
}

function inferContentType(key) {
  const extension = (key.split('.').pop() || '').toLowerCase();

  switch (extension) {
    case 'html':
      return 'text/html; charset=utf-8';
    case 'css':
      return 'text/css; charset=utf-8';
    case 'js':
    case 'mjs':
      return 'application/javascript; charset=utf-8';
    case 'json':
      return 'application/json; charset=utf-8';
    case 'txt':
      return 'text/plain; charset=utf-8';
    case 'xml':
      return 'application/xml; charset=utf-8';
    case 'svg':
      return 'image/svg+xml';
    case 'png':
      return 'image/png';
    case 'jpg':
    case 'jpeg':
      return 'image/jpeg';
    case 'gif':
      return 'image/gif';
    case 'webp':
      return 'image/webp';
    case 'ico':
      return 'image/x-icon';
    case 'woff':
      return 'font/woff';
    case 'woff2':
      return 'font/woff2';
    case 'ttf':
      return 'font/ttf';
    case 'otf':
      return 'font/otf';
    case 'mp4':
      return 'video/mp4';
    case 'webm':
      return 'video/webm';
    case 'pdf':
      return 'application/pdf';
    default:
      return DEFAULT_CONTENT_TYPE;
  }
}
