# BARON SSO PKCE Setup

이 사이트는 정적 HTML 중심 구조이므로, 이번 변경은 브라우저에서 BARON-SSO PKCE 로그인을 먼저 통과한 사용자만 화면을 보게 하는 1차 게이트입니다.

완전한 접근 통제는 별도로 필요합니다.

- HTML, JS, 이미지 원본까지 외부 공개를 막으려면 웹서버 또는 프록시에서 인증 전 차단이 필요합니다.
- 현재 구현만으로는 브라우저 렌더링 진입은 막지만, 공개 정적 파일 URL 자체를 서버가 차단하지는 않습니다.

## 적용 위치

- 메인 공통 진입: `assets/js/common.js`
- 영문 공통 진입: `assets/js/eng/common.js`
- TOVA 레거시 공통 진입: `ko/tova/js/common.js`, `en/tova/js/common.js`
- EGBIM 레거시 공통 진입: `ko/egbim/js/common.js`, `en/egbim/js/common.js`
- PKCE 인증 모듈: `assets/js/baron-sso-auth.js`
- 환경 설정: `assets/js/baron-sso-config.js`

## 필수 설정

`assets/js/baron-sso-config.js`에서 아래 값을 채우고 `enabled`를 `true`로 바꿉니다.

```js
export default {
  enabled: true,
  clientId: "b5821f81-da7a-4778-ba97-7742e4ff4c39",
  authorizeUrl: "https://app.brsw.kr/oidc/oauth2/auth",
  tokenUrl: "https://app.brsw.kr/oidc/oauth2/token",
  logoutUrl: "https://app.brsw.kr/oidc/oauth2/sessions/logout",
  userInfoUrl: "https://app.brsw.kr/oidc/userinfo",
  scope: "openid",
  redirectUri: "https://baroncs.co.kr/callback.html",
  postLogoutRedirectUri: "https://baroncs.co.kr/",
  allowedEmailDomains: [],
  allowedEmails: [],
  requiredGroups: [],
  groupClaim: "groups",
  publicPaths: [],
  extraAuthorizeParams: {},
  extraTokenParams: {},
};
```

## 설정 기준

- `redirectUri`: SSO가 로그인 후 되돌려줄 URI입니다. 등록된 redirect URI와 정확히 일치해야 합니다.
- 현재 배포 기준 콜백 엔드포인트는 `https://baroncs.co.kr/callback.html`입니다.
- 로컬에서 `/baron` 하위로 테스트하면 코드가 자동으로 `http://호스트/baron/callback.html`과 `http://호스트/baron/`을 사용합니다.
- `postLogoutRedirectUri`: 로그아웃 후 복귀할 URI입니다.
- `allowedEmailDomains`: 이 도메인으로 끝나는 메일만 허용합니다. 현재 BARON-SSO에서 어떤 claim이 내려오는지 확정 전이라 기본값은 비워 두었습니다.
- `allowedEmails`: 특정 사용자만 허용할 때 사용합니다. 값이 있으면 이 목록을 먼저 통과해야 합니다.
- `requiredGroups`: SSO 토큰 또는 userinfo 응답의 그룹 값으로 추가 제한할 때 사용합니다.
- `groupClaim`: 그룹 배열이 들어있는 claim 이름입니다. 기본은 `groups`입니다.
- `publicPaths`: 인증 없이 열어둘 경로 prefix 목록입니다. 예를 들어 `/recruit/`를 열어둘 수 있습니다.
- `extraAuthorizeParams`: `audience`, `resource`, `prompt` 같은 인가 요청 추가 파라미터가 필요할 때 사용합니다.
- `extraTokenParams`: 토큰 교환 시 추가 파라미터가 필요할 때 사용합니다.

## IDP 등록 체크리스트

- Authorization Code + PKCE 활성화
- 클라이언트 타입을 브라우저용 public client로 등록
- `redirectUri` 허용 목록 등록
- `postLogoutRedirectUri` 허용 목록 등록
- CORS에서 `https://baroncs.co.kr` 허용
- 운영 앱은 `https://baroncs.co.kr/callback.html`을 redirect URI로 등록
- 로컬 테스트가 필요하면 `http://172.16.9.44/baron/callback.html` 같은 로컬 callback URL도 별도 등록
- 로컬 테스트가 필요하면 `http://172.16.9.44` origin에 대한 CORS 허용 여부 확인
- `tokenUrl`과 `userInfoUrl`이 브라우저 호출을 허용하는지 확인
- 토큰 또는 userinfo에 `email` 또는 `preferred_username` 포함 여부 확인
- 그룹 제한이 필요하면 토큰 또는 userinfo에 그룹 claim 포함 확인

## 동작 방식

1. 페이지 진입 시 공통 스크립트가 먼저 SSO 세션을 확인합니다.
2. 세션이 없으면 PKCE verifier/challenge를 생성하고 SSO 로그인으로 리다이렉트합니다.
3. `code`가 돌아오면 토큰 교환 후 사용자 claim을 검사합니다.
4. 허용된 내부 사용자면 원래 페이지를 렌더링합니다.
5. 허용되지 않으면 접근 불가 오버레이를 유지합니다.

## 운영 권장

- 가능하면 Cloudflare Access, Nginx auth_request, 사내 프록시 같은 서버 측 인증을 앞단에 두세요.
- 현재 PKCE 게이트는 사용자 경험 제어와 1차 접근 제한에는 적합하지만, 정적 파일 원본 보호 수단으로는 충분하지 않습니다.
- SSO 설정 변경 후 브라우저 로컬스토리지의 `baron_sso_session`을 지우고 다시 테스트하세요.