const currentUrl = new URL(window.location.href);
const appPathSegments = currentUrl.pathname.split("/").filter(Boolean);
const rootMarkerSegments = ["ko", "en", "callback", "assets", "protected", "public", "recruit"];
const rootPrefix = appPathSegments.length && !rootMarkerSegments.includes(appPathSegments[0])
  ? `/${appPathSegments[0]}`
  : "";
const appOrigin = currentUrl.origin;
const isProductionHost = currentUrl.hostname === "baroncs.co.kr";
const defaultRedirectUri = isProductionHost
  ? "https://baroncs.co.kr/callback.html"
  : `${appOrigin}${rootPrefix}/callback.html`;
const defaultPostLogoutRedirectUri = isProductionHost
  ? "https://baroncs.co.kr/"
  : `${rootPrefix}/`;

const productionConfig = {
  clientId: "b5821f81-da7a-4778-ba97-7742e4ff4c39",
  authorizeUrl: "https://app.brsw.kr/oidc/oauth2/auth",
  tokenUrl: "https://app.brsw.kr/oidc/oauth2/token",
  logoutUrl: "https://app.brsw.kr/oidc/oauth2/sessions/logout",
  userInfoUrl: "https://app.brsw.kr/oidc/userinfo",
  scope: "openid",
};

const stagingConfig = {
  clientId: "037b546a-86b7-4ff4-bdaf-c41c98fb6766",
  authorizeUrl: "https://sso.hmac.kr/oidc/oauth2/auth",
  tokenUrl: "https://sso.hmac.kr/oidc/oauth2/token",
  logoutUrl: "https://sso.hmac.kr/oidc/oauth2/sessions/logout",
  userInfoUrl: "https://sso.hmac.kr/oidc/userinfo",
  scope: "openid tenants profile email",
};

const activeConfig = isProductionHost ? productionConfig : stagingConfig;

export default {
  enabled: true,
  clientId: activeConfig.clientId,
  authorizeUrl: activeConfig.authorizeUrl,
  tokenUrl: activeConfig.tokenUrl,
  logoutUrl: activeConfig.logoutUrl,
  userInfoUrl: activeConfig.userInfoUrl,
  scope: activeConfig.scope,
  redirectUri: defaultRedirectUri,
  postLogoutRedirectUri: defaultPostLogoutRedirectUri,
  allowedEmailDomains: [],
  allowedEmails: [],
  requiredGroups: [],
  groupClaim: "groups",
  publicPaths: [],
  extraAuthorizeParams: {},
  extraTokenParams: {},
};
