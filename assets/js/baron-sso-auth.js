import baseConfig from "./baron-sso-config.js?v=20260721-test1";

const STORAGE_KEY = "baron_sso_session";
const PENDING_LOGIN_KEY = "baron_sso_pending_login";
const STATE_KEY = "baron_sso_state";
const VERIFIER_KEY = "baron_sso_code_verifier";
const RETURN_TO_KEY = "baron_sso_return_to";
const FORCE_LOGIN_KEY = "baron_sso_force_login";
const OVERLAY_ID = "baron-sso-overlay";
const STYLE_ID = "baron-sso-style";

const messages = {
  ko: {
    loadingTitle: "BARON SSO 확인 중",
    loadingDescription: "접근 권한을 확인하고 있습니다.",
    redirectTitle: "BARON SSO 로그인으로 이동합니다",
    redirectDescription: "내부 사용자 인증이 필요합니다.",
    redirectAction: "다시 로그인",
    unauthorizedTitle: "접근 권한이 없습니다",
    unauthorizedDescription: "BARON 내부 사용자 계정으로 로그인해야 합니다.",
    retryAction: "다시 로그인",
    configTitle: "BARON SSO 설정이 필요합니다",
    configDescription: "clientId, authorizeUrl, tokenUrl 값을 먼저 설정하세요.",
    exchangeTitle: "로그인 처리에 실패했습니다",
    exchangeDescription: "인증 응답을 처리하지 못했습니다. 다시 로그인해 주세요.",
    logoutAction: "로그아웃",
  },
  en: {
    loadingTitle: "Checking BARON SSO",
    loadingDescription: "Verifying your access.",
    redirectTitle: "Redirecting to BARON SSO",
    redirectDescription: "Internal user authentication is required.",
    redirectAction: "Sign in again",
    unauthorizedTitle: "Access denied",
    unauthorizedDescription: "You must sign in with an internal BARON account.",
    retryAction: "Sign in again",
    configTitle: "BARON SSO configuration required",
    configDescription: "Set clientId, authorizeUrl, and tokenUrl before enabling the gate.",
    exchangeTitle: "Login failed",
    exchangeDescription: "The authentication response could not be processed. Please try again.",
    logoutAction: "Logout",
  },
};

function mergeConfig(overrides = {}) {
  const windowConfig = window.BARON_SSO_CONFIG || {};
  const config = {
    ...baseConfig,
    ...windowConfig,
    ...overrides,
  };

  config.allowedEmailDomains = normalizeArray(config.allowedEmailDomains);
  config.allowedEmails = normalizeArray(config.allowedEmails);
  config.requiredGroups = normalizeArray(config.requiredGroups);
  config.publicPaths = normalizeArray(config.publicPaths);
  config.extraAuthorizeParams = config.extraAuthorizeParams || {};
  config.extraTokenParams = config.extraTokenParams || {};
  config.locale = config.locale || detectLocale();

  return config;
}

function normalizeArray(value) {
  return Array.isArray(value) ? value.filter(Boolean) : [];
}

function getRootPrefix(pathname = window.location.pathname) {
  const pathSegments = pathname.split("/").filter(Boolean);
  const rootMarkerSegments = ["ko", "en", "callback", "assets", "protected", "public", "recruit"];
  return pathSegments.length && !rootMarkerSegments.includes(pathSegments[0])
    ? `/${pathSegments[0]}`
    : "";
}

function normalizePath(path) {
  if (!path) {
    return "/";
  }

  const normalizedPath = path.replace(/\/index\.html$/i, "/");

  if (normalizedPath.length > 1 && normalizedPath.endsWith("/")) {
    return normalizedPath.slice(0, -1);
  }

  return normalizedPath;
}

function detectLocale() {
  return window.location.pathname.startsWith("/en/") ? "en" : "ko";
}

function isLocalEnvironment() {
  return window.location.hostname !== "baroncs.co.kr";
}

function getMessage(config, key) {
  const localeMessages = messages[config.locale] || messages.ko;
  return localeMessages[key];
}

function installStyles() {
  if (document.getElementById(STYLE_ID)) {
    return;
  }

  const style = document.createElement("style");
  style.id = STYLE_ID;
  style.textContent = `
    html[data-baron-auth-pending="true"] body > :not(#${OVERLAY_ID}) {
      visibility: hidden;
    }

    #${OVERLAY_ID} {
      position: fixed;
      inset: 0;
      z-index: 99999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
      background: rgba(9, 17, 27, 0.78);
      font-family: "Pretendard", "Noto Sans KR", sans-serif;
    }

    #${OVERLAY_ID}.is-visible {
      display: flex;
    }

    #${OVERLAY_ID} .baron-sso-panel {
      width: min(480px, 100%);
      padding: 32px 28px;
      border-radius: 20px;
      background: #ffffff;
      box-shadow: 0 24px 80px rgba(0, 0, 0, 0.18);
      color: #111827;
      text-align: center;
    }

    #${OVERLAY_ID} .baron-sso-title {
      margin: 0;
      font-size: 28px;
      font-weight: 700;
      line-height: 1.3;
    }

    #${OVERLAY_ID} .baron-sso-description {
      margin: 12px 0 0;
      font-size: 16px;
      line-height: 1.6;
      color: #4b5563;
    }

    #${OVERLAY_ID} .baron-sso-actions {
      display: flex;
      gap: 12px;
      justify-content: center;
      margin-top: 24px;
      flex-wrap: wrap;
    }

    #${OVERLAY_ID} button {
      min-width: 160px;
      padding: 12px 18px;
      border: 0;
      border-radius: 999px;
      background: #101828;
      color: #ffffff;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
    }

    #${OVERLAY_ID} button.baron-sso-secondary {
      background: #e5e7eb;
      color: #111827;
    }
  `;
  document.head.appendChild(style);
}

function waitForBody() {
  if (document.body) {
    return Promise.resolve();
  }

  return new Promise((resolve) => {
    document.addEventListener("DOMContentLoaded", resolve, { once: true });
  });
}

function setPending(isPending) {
  document.documentElement.toggleAttribute("data-baron-auth-pending", isPending);
}

function ensureOverlay() {
  let overlay = document.getElementById(OVERLAY_ID);

  if (!overlay) {
    overlay = document.createElement("div");
    overlay.id = OVERLAY_ID;
    overlay.innerHTML = `
      <div class="baron-sso-panel">
        <h1 class="baron-sso-title"></h1>
        <p class="baron-sso-description"></p>
        <div class="baron-sso-actions"></div>
      </div>
    `;
    document.body.appendChild(overlay);
  }

  return overlay;
}

function renderOverlay(config, options) {
  installStyles();
  const overlay = ensureOverlay();
  const title = overlay.querySelector(".baron-sso-title");
  const description = overlay.querySelector(".baron-sso-description");
  const actions = overlay.querySelector(".baron-sso-actions");

  title.textContent = options.title;
  description.textContent = options.description;
  actions.innerHTML = "";

  (options.actions || []).forEach((action) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = action.label;
    if (action.secondary) {
      button.className = "baron-sso-secondary";
    }
    button.addEventListener("click", action.onClick);
    actions.appendChild(button);
  });

  overlay.classList.add("is-visible");
  setPending(true);
}

function hideOverlay() {
  const overlay = document.getElementById(OVERLAY_ID);
  if (overlay) {
    overlay.classList.remove("is-visible");
  }
  setPending(false);
}

function isConfigured(config) {
  return Boolean(config.clientId && config.authorizeUrl && config.tokenUrl);
}

function isPublicPath(config) {
  const currentPath = normalizePath(window.location.pathname);
  return config.publicPaths.some((entry) => {
    const normalizedEntry = normalizePath(entry);
    return currentPath === normalizedEntry || currentPath.startsWith(`${normalizedEntry}/`);
  });
}

function buildRedirectUri(config) {
  return config.redirectUri || `${window.location.origin}${window.location.pathname}`;
}

function getCallbackPaths(config) {
  const configuredPath = normalizePath(new URL(buildRedirectUri(config)).pathname);
  const rootPrefix = getRootPrefix();
  const candidatePaths = [
    configuredPath,
    `${rootPrefix}/callback.html`,
    `${rootPrefix}/callback/index.html`,
  ];

  return [...new Set(candidatePaths)];
}

function buildReturnToUrl() {
  const currentUrl = new URL(window.location.href);
  currentUrl.search = "";
  currentUrl.hash = "";
  return currentUrl.toString();
}

function isCallbackPath(config) {
  return getCallbackPaths(config).includes(normalizePath(window.location.pathname));
}

function getCryptoObject() {
  return window.crypto || window.msCrypto || null;
}

function fillRandomValues(bytes) {
  const cryptoObject = getCryptoObject();

  if (cryptoObject?.getRandomValues) {
    cryptoObject.getRandomValues(bytes);
    return bytes;
  }

  for (let index = 0; index < bytes.length; index += 1) {
    bytes[index] = Math.floor(Math.random() * 256);
  }

  return bytes;
}

function rightRotate(value, amount) {
  return (value >>> amount) | (value << (32 - amount));
}

function sha256Fallback(message) {
  const constants = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
  ];
  const initialHash = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
  ];
  const bytes = new TextEncoder().encode(message);
  const bitLength = bytes.length * 8;
  const paddedLength = (((bytes.length + 9 + 63) >> 6) << 6);
  const padded = new Uint8Array(paddedLength);
  padded.set(bytes);
  padded[bytes.length] = 0x80;

  const bitLengthHigh = Math.floor(bitLength / 0x100000000);
  const bitLengthLow = bitLength >>> 0;
  padded[padded.length - 8] = (bitLengthHigh >>> 24) & 0xff;
  padded[padded.length - 7] = (bitLengthHigh >>> 16) & 0xff;
  padded[padded.length - 6] = (bitLengthHigh >>> 8) & 0xff;
  padded[padded.length - 5] = bitLengthHigh & 0xff;
  padded[padded.length - 4] = (bitLengthLow >>> 24) & 0xff;
  padded[padded.length - 3] = (bitLengthLow >>> 16) & 0xff;
  padded[padded.length - 2] = (bitLengthLow >>> 8) & 0xff;
  padded[padded.length - 1] = bitLengthLow & 0xff;

  const words = new Uint32Array(64);
  const hash = initialHash.slice();

  for (let offset = 0; offset < padded.length; offset += 64) {
    for (let index = 0; index < 16; index += 1) {
      const position = offset + index * 4;
      words[index] = (
        (padded[position] << 24) |
        (padded[position + 1] << 16) |
        (padded[position + 2] << 8) |
        padded[position + 3]
      ) >>> 0;
    }

    for (let index = 16; index < 64; index += 1) {
      const sigma0 = rightRotate(words[index - 15], 7) ^ rightRotate(words[index - 15], 18) ^ (words[index - 15] >>> 3);
      const sigma1 = rightRotate(words[index - 2], 17) ^ rightRotate(words[index - 2], 19) ^ (words[index - 2] >>> 10);
      words[index] = (words[index - 16] + sigma0 + words[index - 7] + sigma1) >>> 0;
    }

    let a = hash[0];
    let b = hash[1];
    let c = hash[2];
    let d = hash[3];
    let e = hash[4];
    let f = hash[5];
    let g = hash[6];
    let h = hash[7];

    for (let index = 0; index < 64; index += 1) {
      const sigma1 = rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25);
      const choice = (e & f) ^ (~e & g);
      const temp1 = (h + sigma1 + choice + constants[index] + words[index]) >>> 0;
      const sigma0 = rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22);
      const majority = (a & b) ^ (a & c) ^ (b & c);
      const temp2 = (sigma0 + majority) >>> 0;

      h = g;
      g = f;
      f = e;
      e = (d + temp1) >>> 0;
      d = c;
      c = b;
      b = a;
      a = (temp1 + temp2) >>> 0;
    }

    hash[0] = (hash[0] + a) >>> 0;
    hash[1] = (hash[1] + b) >>> 0;
    hash[2] = (hash[2] + c) >>> 0;
    hash[3] = (hash[3] + d) >>> 0;
    hash[4] = (hash[4] + e) >>> 0;
    hash[5] = (hash[5] + f) >>> 0;
    hash[6] = (hash[6] + g) >>> 0;
    hash[7] = (hash[7] + h) >>> 0;
  }

  const digest = new Uint8Array(32);
  hash.forEach((value, index) => {
    const position = index * 4;
    digest[position] = (value >>> 24) & 0xff;
    digest[position + 1] = (value >>> 16) & 0xff;
    digest[position + 2] = (value >>> 8) & 0xff;
    digest[position + 3] = value & 0xff;
  });

  return digest;
}

function createRandomString(length = 64) {
  const bytes = new Uint8Array(length);
  fillRandomValues(bytes);
  return base64UrlEncode(bytes).slice(0, length);
}

function base64UrlEncode(input) {
  const bytes = input instanceof Uint8Array ? input : new TextEncoder().encode(String(input));
  let binary = "";

  bytes.forEach((byte) => {
    binary += String.fromCharCode(byte);
  });

  return window.btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

async function createCodeChallenge(verifier) {
  const cryptoObject = getCryptoObject();

  if (cryptoObject?.subtle?.digest) {
    const digest = await cryptoObject.subtle.digest("SHA-256", new TextEncoder().encode(verifier));
    return base64UrlEncode(new Uint8Array(digest));
  }

  return base64UrlEncode(sha256Fallback(verifier));
}

function savePendingLogin(state, verifier, returnTo) {
  sessionStorage.setItem(STATE_KEY, state);
  sessionStorage.setItem(VERIFIER_KEY, verifier);
  sessionStorage.setItem(RETURN_TO_KEY, returnTo);
  localStorage.setItem(PENDING_LOGIN_KEY, JSON.stringify({ state, verifier, returnTo }));
}

function clearPendingLogin() {
  sessionStorage.removeItem(STATE_KEY);
  sessionStorage.removeItem(VERIFIER_KEY);
  sessionStorage.removeItem(RETURN_TO_KEY);
  localStorage.removeItem(PENDING_LOGIN_KEY);
}

function loadPendingLogin() {
  const state = sessionStorage.getItem(STATE_KEY);
  const verifier = sessionStorage.getItem(VERIFIER_KEY);
  const returnTo = sessionStorage.getItem(RETURN_TO_KEY);

  if (state && verifier) {
    return {
      state,
      verifier,
      returnTo,
    };
  }

  const raw = localStorage.getItem(PENDING_LOGIN_KEY);

  if (!raw) {
    return null;
  }

  try {
    const pendingLogin = JSON.parse(raw);

    if (!pendingLogin?.state || !pendingLogin?.verifier) {
      localStorage.removeItem(PENDING_LOGIN_KEY);
      return null;
    }

    sessionStorage.setItem(STATE_KEY, pendingLogin.state);
    sessionStorage.setItem(VERIFIER_KEY, pendingLogin.verifier);
    if (pendingLogin.returnTo) {
      sessionStorage.setItem(RETURN_TO_KEY, pendingLogin.returnTo);
    }

    return pendingLogin;
  } catch {
    localStorage.removeItem(PENDING_LOGIN_KEY);
    return null;
  }
}

function markForceLogin() {
  sessionStorage.setItem(FORCE_LOGIN_KEY, "1");
}

function consumeForceLogin() {
  const shouldForce = sessionStorage.getItem(FORCE_LOGIN_KEY) === "1";
  sessionStorage.removeItem(FORCE_LOGIN_KEY);
  return shouldForce;
}

function saveSession(session) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(session));
}

function loadSession() {
  const raw = localStorage.getItem(STORAGE_KEY);

  if (!raw) {
    return null;
  }

  try {
    return JSON.parse(raw);
  } catch {
    localStorage.removeItem(STORAGE_KEY);
    return null;
  }
}

function clearSession() {
  localStorage.removeItem(STORAGE_KEY);
}

function isExpired(session) {
  if (!session || !session.expiresAt) {
    return true;
  }

  return Date.now() >= Number(session.expiresAt);
}

function decodeJwt(token) {
  if (!token || token.split(".").length < 2) {
    return null;
  }

  try {
    const payload = token.split(".")[1].replace(/-/g, "+").replace(/_/g, "/");
    const normalized = payload.padEnd(payload.length + ((4 - (payload.length % 4)) % 4), "=");
    return JSON.parse(window.atob(normalized));
  } catch {
    return null;
  }
}

async function fetchUserInfo(config, accessToken) {
  if (!config.userInfoUrl || !accessToken) {
    return null;
  }

  const response = await fetch(config.userInfoUrl, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });

  if (!response.ok) {
    throw new Error(`User info request failed: ${response.status}`);
  }

  return response.json();
}

async function resolveProfile(config, tokenResult) {
  const idTokenClaims = decodeJwt(tokenResult.id_token);
  const accessTokenClaims = decodeJwt(tokenResult.access_token);

  if (idTokenClaims) {
    return idTokenClaims;
  }

  if (accessTokenClaims) {
    return accessTokenClaims;
  }

  return fetchUserInfo(config, tokenResult.access_token);
}

function readProfileEmail(profile) {
  return (
    profile?.email ||
    profile?.preferred_username ||
    profile?.upn ||
    profile?.unique_name ||
    ""
  )
    .trim()
    .toLowerCase();
}

function hasRequiredGroup(config, profile) {
  if (!config.requiredGroups.length) {
    return true;
  }

  const groupValue = profile?.[config.groupClaim];
  const groups = Array.isArray(groupValue) ? groupValue : typeof groupValue === "string" ? [groupValue] : [];
  return config.requiredGroups.some((group) => groups.includes(group));
}

function isAuthorized(config, profile) {
  if (!profile) {
    return false;
  }

  const email = readProfileEmail(profile);

  if (config.allowedEmails.length && !config.allowedEmails.includes(email)) {
    return false;
  }

  if (config.allowedEmailDomains.length) {
    const hasDomain = config.allowedEmailDomains.some((domain) => email.endsWith(`@${domain.toLowerCase()}`));
    if (!hasDomain) {
      return false;
    }
  }

  return hasRequiredGroup(config, profile);
}

async function exchangeCode(config, code, verifier) {
  const body = new URLSearchParams({
    grant_type: "authorization_code",
    client_id: config.clientId,
    code,
    code_verifier: verifier,
    redirect_uri: buildRedirectUri(config),
  });

  Object.entries(config.extraTokenParams).forEach(([key, value]) => {
    if (value !== undefined && value !== null) {
      body.set(key, String(value));
    }
  });

  const response = await fetch(config.tokenUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body,
  });

  if (!response.ok) {
    let errorDetail = "";

    try {
      const responseText = await response.text();
      if (responseText) {
        errorDetail = responseText;
      }
    } catch {
      errorDetail = "";
    }

    const errorMessage = errorDetail
      ? `Token request failed: ${response.status} ${errorDetail}`
      : `Token request failed: ${response.status}`;

    throw new Error(errorMessage);
  }

  return response.json();
}

async function handleCallback(config) {
  const currentUrl = new URL(window.location.href);
  const code = currentUrl.searchParams.get("code");
  const state = currentUrl.searchParams.get("state");

  if (!code || !state) {
    return false;
  }

  const pendingLogin = loadPendingLogin();
  const expectedState = pendingLogin?.state || null;
  const verifier = pendingLogin?.verifier || null;
  const returnTo = pendingLogin?.returnTo || buildRedirectUri(config);

  if (!expectedState || !verifier || expectedState !== state) {
    clearPendingLogin();
    throw new Error("Invalid OAuth state");
  }

  const tokenResult = await exchangeCode(config, code, verifier);
  const profile = await resolveProfile(config, tokenResult);

  if (!isAuthorized(config, profile)) {
    clearPendingLogin();
    clearSession();
    throw new Error("User is not authorized");
  }

  const expiresIn = Number(tokenResult.expires_in || 3600);
  saveSession({
    accessToken: tokenResult.access_token,
    idToken: tokenResult.id_token || "",
    tokenType: tokenResult.token_type || "Bearer",
    profile,
    expiresAt: Date.now() + Math.max(expiresIn - 30, 30) * 1000,
  });

  clearPendingLogin();
  return {
    handled: true,
    returnTo,
  };
}

async function startLogin(config) {
  const verifier = createRandomString(96);
  const state = createRandomString(48);
  const challenge = await createCodeChallenge(verifier);
  const returnTo = buildReturnToUrl();
  const shouldForceLogin = consumeForceLogin();

  savePendingLogin(state, verifier, returnTo);

  const authorizeUrl = new URL(config.authorizeUrl);
  authorizeUrl.searchParams.set("response_type", "code");
  authorizeUrl.searchParams.set("client_id", config.clientId);
  authorizeUrl.searchParams.set("redirect_uri", buildRedirectUri(config));
  authorizeUrl.searchParams.set("scope", config.scope);
  authorizeUrl.searchParams.set("state", state);
  authorizeUrl.searchParams.set("code_challenge", challenge);
  authorizeUrl.searchParams.set("code_challenge_method", "S256");

  Object.entries(config.extraAuthorizeParams).forEach(([key, value]) => {
    if (value !== undefined && value !== null) {
      authorizeUrl.searchParams.set(key, String(value));
    }
  });

  if (shouldForceLogin && !authorizeUrl.searchParams.has("prompt")) {
    authorizeUrl.searchParams.set("prompt", "login");
  }

  renderOverlay(config, {
    title: getMessage(config, "redirectTitle"),
    description: getMessage(config, "redirectDescription"),
    actions: [
      {
        label: getMessage(config, "redirectAction"),
        onClick: () => {
          window.location.assign(authorizeUrl.toString());
        },
      },
    ],
  });

  window.location.assign(authorizeUrl.toString());
}

async function restoreSession(config) {
  const session = loadSession();

  if (!session || isExpired(session)) {
    clearSession();
    return null;
  }

  if (!isAuthorized(config, session.profile)) {
    clearSession();
    return null;
  }

  return session;
}

function attachLogout(config) {
  window.baronSsoLogout = () => {
    const session = loadSession();
    const idTokenHint = session?.idToken;
    const localRedirectTarget = config.postLogoutRedirectUri || `${window.location.origin}/`;
    const shouldUseLocalOnlyLogout = isLocalEnvironment() || !config.logoutUrl || !idTokenHint;

    clearPendingLogin();
    clearSession();
    window.BARON_SSO_SESSION = null;

    if (shouldUseLocalOnlyLogout) {
      markForceLogin();
      window.location.assign(localRedirectTarget);
      return;
    }

    const logoutUrl = new URL(config.logoutUrl);

    logoutUrl.searchParams.set("id_token_hint", idTokenHint);
    logoutUrl.searchParams.set("client_id", config.clientId);

    if (config.postLogoutRedirectUri) {
      logoutUrl.searchParams.set("post_logout_redirect_uri", config.postLogoutRedirectUri);
    }

    window.location.assign(logoutUrl.toString());
  };
}

export async function ensureBaronSsoAuth(overrides = {}) {
  const config = mergeConfig(overrides);
  const currentUrl = new URL(window.location.href);
  const hasCallbackParams = currentUrl.searchParams.has("code") || currentUrl.searchParams.has("state");
  const publicPath = isPublicPath(config);

  if (!config.enabled) {
    return { status: "disabled" };
  }

  attachLogout(config);

  if (publicPath && !config.forceAuth) {
    const session = await restoreSession(config);
    if (session) {
      window.BARON_SSO_SESSION = session;
      hideOverlay();
      return { status: "authenticated-public", session };
    }

    return { status: "public" };
  }

  await waitForBody();
  renderOverlay(config, {
    title: getMessage(config, "loadingTitle"),
    description: getMessage(config, "loadingDescription"),
  });

  if (!isConfigured(config)) {
    renderOverlay(config, {
      title: getMessage(config, "configTitle"),
      description: getMessage(config, "configDescription"),
    });
    return { status: "misconfigured" };
  }

  try {
    if (isCallbackPath(config) && !hasCallbackParams) {
      window.location.replace(config.postLogoutRedirectUri || `${window.location.origin}/`);
      return { status: "callback-idle" };
    }

    const callbackResult = await handleCallback(config);
    if (callbackResult?.handled) {
      const destination = callbackResult.returnTo || `${window.location.origin}/`;
      if (destination !== window.location.href) {
        window.location.replace(destination);
        return { status: "redirected", returnTo: destination };
      }
    }

    const session = await restoreSession(config);
    if (session) {
      window.BARON_SSO_SESSION = session;
      hideOverlay();
      return { status: "authenticated", session };
    }

    await startLogin(config);
    return { status: "redirecting" };
  } catch (error) {
    console.error("BARON SSO authentication failed.", error);

    const isUnauthorized = error.message === "User is not authorized";
    const detailDescription = isUnauthorized
      ? getMessage(config, "unauthorizedDescription")
      : isLocalEnvironment()
        ? `${getMessage(config, "exchangeDescription")} (${error.message})`
        : getMessage(config, "exchangeDescription");

    clearSession();
    clearPendingLogin();
    renderOverlay(config, {
      title: getMessage(config, "unauthorizedTitle"),
      description: detailDescription,
      actions: [
        {
          label: getMessage(config, "retryAction"),
          onClick: () => {
            startLogin(config);
          },
        },
        {
          label: getMessage(config, "logoutAction"),
          secondary: true,
          onClick: () => {
            window.baronSsoLogout();
          },
        },
      ],
    });
    return { status: "failed", error };
  }
}
