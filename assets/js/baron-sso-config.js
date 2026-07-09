const currentUrl = new URL(window.location.href);
const rootPrefix = currentUrl.pathname.startsWith("/baron/") ? "/baron" : "";
const appOrigin = currentUrl.origin;
const defaultRedirectUri = `${appOrigin}${rootPrefix}/callback.html`;
const defaultPostLogoutRedirectUri = `${appOrigin}${rootPrefix}/`;

export default {
  enabled: true,
  clientId: "b5821f81-da7a-4778-ba97-7742e4ff4c39",
  authorizeUrl: "https://app.brsw.kr/oidc/oauth2/auth",
  tokenUrl: "https://app.brsw.kr/oidc/oauth2/token",
  logoutUrl: "https://app.brsw.kr/oidc/oauth2/sessions/logout",
  userInfoUrl: "https://app.brsw.kr/oidc/userinfo",
  scope: "openid",
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