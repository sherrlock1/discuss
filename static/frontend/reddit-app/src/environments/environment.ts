// Environment configuration for development
// For local development, use localhost URLs
// For deployment, these can be overridden via build configuration
export const environment = {
  production: false,
  baseUrl: '/api/v1/',
  serverUrl: (typeof window !== 'undefined' && window.location.hostname === 'localhost') 
    ? 'http://localhost:8000' 
    : 'https://work-1-otvuwyhcdtyibpym.prod-runtime.all-hands.dev',
  appUrl: (typeof window !== 'undefined' && window.location.hostname === 'localhost') 
    ? 'http://localhost:4200' 
    : 'https://work-2-otvuwyhcdtyibpym.prod-runtime.all-hands.dev',
  loginUrl: (typeof window !== 'undefined' && window.location.hostname === 'localhost') 
    ? 'http://localhost:4200/sign-in' 
    : 'https://work-2-otvuwyhcdtyibpym.prod-runtime.all-hands.dev/sign-in',
  staticUrl: '../assets/images/'
};
