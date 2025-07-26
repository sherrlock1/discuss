export const environment = {
  production: true,
  baseUrl: '/api/v1/',
  // Production URLs - these should be configured for your actual deployment
  serverUrl: process.env['DJANGO_SERVER_URL'] || 'https://your-django-server.com',
  appUrl: process.env['ANGULAR_APP_URL'] || 'https://your-angular-app.com',
  loginUrl: process.env['LOGIN_URL'] || 'https://your-angular-app.com/sign-in',
  staticUrl: '../assets/images/'
};
