# Known Issues

This document outlines known issues, limitations, and workarounds for the Django Reddit Clone application.

## 🚨 Critical Issues

### 1. Froala WYSIWYG Editor Compatibility
**Status**: ❌ **Broken**  
**Affected Components**: Post creation, comment editing  
**Description**: The Froala editor has TypeScript compatibility issues with Angular 10 and Node.js 22+.

**Error Details**:
```
node_modules/froala-editor/index.d.ts:1605:15 - error TS1005: ';' expected.
node_modules/froala-editor/index.d.ts:1605:45 - error TS1109: Expression expected.
```

**Current Workaround**:
- Froala editor imports are commented out in:
  - `src/app/app.module.ts`
  - `src/app/post/create-post/create-post.component.ts`
- Post creation falls back to basic text input

**Impact**: 
- ❌ No rich text editing for posts
- ❌ No WYSIWYG formatting options
- ✅ Basic text posting still works

**Potential Solutions**:
1. Upgrade to compatible Froala version
2. Replace with alternative editor (TinyMCE, CKEditor)
3. Implement custom rich text solution

---

## ⚠️ Compatibility Issues

### 2. Node.js OpenSSL Legacy Provider Required
**Status**: ⚠️ **Workaround Available**  
**Affected**: Angular development server  
**Description**: Angular 10 with Node.js 22+ requires legacy OpenSSL provider.

**Error**:
```
Error: error:0308010C:digital envelope routines::unsupported
```

**Workaround**:
```bash
NODE_OPTIONS="--openssl-legacy-provider" ng serve
```

**Impact**: 
- ⚠️ Requires special Node.js flags
- ✅ Application runs normally with workaround

### 3. TypeScript Strict Mode Compatibility
**Status**: ⚠️ **Workaround Applied**  
**Affected**: Angular compilation  
**Description**: Legacy dependencies have TypeScript compatibility issues.

**Workaround Applied**:
```json
// tsconfig.json
{
  "compilerOptions": {
    "skipLibCheck": true,
    "skipDefaultLibCheck": true
  }
}
```

**Impact**:
- ⚠️ Reduced type checking strictness
- ✅ Compilation succeeds

---

## 🔧 Configuration Issues

### 4. CORS Configuration for Deployment
**Status**: ✅ **Resolved**  
**Description**: Cross-origin requests between Angular frontend and Django backend required CORS configuration.

**Solution Applied**:
```python
# settings.py
CORS_ALLOWED_ORIGINS = [
    "https://work-1-otvuwyhcdtyibpym.prod-runtime.all-hands.dev",
    "https://work-2-otvuwyhcdtyibpym.prod-runtime.all-hands.dev",
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]
```

### 5. Static File Serving in Production
**Status**: ✅ **Resolved**  
**Description**: Django needed middleware for serving static files in production.

**Solution Applied**:
- Added `whitenoise==6.2.0` to requirements.txt
- Configured in Django settings

---

## 📱 Frontend Issues

### 6. Angular Routing Configuration
**Status**: ⚠️ **Partial Issue**  
**Description**: Angular app expects to be served from `/django_reddit` path.

**Current Behavior**:
- ✅ Works: `http://localhost:4200/django_reddit`
- ❌ Fails: `http://localhost:4200/`

**Impact**: 
- ⚠️ Specific URL path required
- ✅ Application functions normally on correct path

### 7. Environment Configuration Hardcoded
**Status**: ⚠️ **Needs Improvement**  
**Description**: Environment URLs are hardcoded in Angular environment files.

**Current State**:
```typescript
// environment.ts
export const environment = {
  serverUrl: 'https://work-1-otvuwyhcdtyibpym.prod-runtime.all-hands.dev',
  appUrl: 'https://work-2-otvuwyhcdtyibpym.prod-runtime.all-hands.dev'
};
```

**Recommendation**: Use environment variables or build-time configuration.

---

## 🗄️ Database Issues

### 8. SQLite in Production
**Status**: ⚠️ **Not Recommended for Production**  
**Description**: Application uses SQLite which is not suitable for production deployment.

**Current State**: 
- ✅ Works for development and testing
- ❌ Not scalable for production use

**Recommendation**: 
- Migrate to PostgreSQL or MySQL for production
- Configure database connection pooling

### 9. Database Migrations Order Dependency
**Status**: ⚠️ **Potential Issue**  
**Description**: Some migrations may have dependency issues if run out of order.

**Workaround**: 
```bash
# If migration issues occur:
python manage.py migrate --run-syncdb
```

---

## 🔐 Security Issues

### 10. Debug Mode in Production
**Status**: ⚠️ **Security Risk**  
**Description**: Django DEBUG mode should be disabled in production.

**Current State**: `DEBUG = True` (for testing)  
**Production Fix**: Set `DEBUG = False` and configure proper error handling

### 11. Secret Key Exposure
**Status**: ⚠️ **Security Risk**  
**Description**: Django secret key should not be hardcoded.

**Recommendation**: Use environment variables for sensitive configuration.

---

## 📦 Dependency Issues

### 12. Outdated Dependencies
**Status**: ⚠️ **Security & Compatibility Risk**  
**Description**: Several dependencies have known vulnerabilities or are outdated.

**Key Outdated Packages**:
- Django 3.1.14 (Latest: 4.2+)
- Angular 10 (Latest: 17+)
- Node.js compatibility issues

**Impact**:
- ⚠️ Security vulnerabilities
- ⚠️ Limited feature support
- ⚠️ Compatibility issues with modern tools

### 13. Package Version Conflicts
**Status**: ⚠️ **Potential Issue**  
**Description**: Some npm packages may have peer dependency warnings.

**Observed Warnings**:
```
npm WARN deprecated packages during installation
```

**Impact**: 
- ⚠️ Build warnings
- ✅ Application still functions

---

## 🧪 Testing Issues

### 14. No Test Suite Configuration
**Status**: ❌ **Missing**  
**Description**: Project lacks comprehensive test configuration.

**Missing Components**:
- Unit tests for Django models/views
- Angular component tests
- Integration tests
- E2E tests

**Impact**: 
- ❌ No automated testing
- ❌ Difficult to verify changes
- ❌ Risk of regressions

---

## 🚀 Performance Issues

### 15. Large Bundle Size
**Status**: ⚠️ **Performance Impact**  
**Description**: Angular application has large bundle sizes.

**Observed**:
```
chunk {vendor} vendor.js, vendor.js.map (vendor) 8.08 MB [initial]
```

**Impact**:
- ⚠️ Slow initial load times
- ⚠️ High bandwidth usage

**Recommendations**:
- Implement lazy loading
- Tree shaking optimization
- Bundle splitting

### 16. No Caching Strategy
**Status**: ⚠️ **Performance Impact**  
**Description**: No caching implemented for API responses or static assets.

**Impact**:
- ⚠️ Repeated API calls
- ⚠️ Slower user experience

---

## 🔄 Workaround Summary

### Quick Fixes Applied
1. **Froala Editor**: Commented out imports
2. **Node.js**: Use `NODE_OPTIONS="--openssl-legacy-provider"`
3. **TypeScript**: Added `skipLibCheck: true`
4. **CORS**: Configured allowed origins
5. **Static Files**: Added whitenoise middleware

### Recommended Long-term Solutions
1. **Upgrade Dependencies**: Plan systematic upgrade to modern versions
2. **Replace Froala**: Implement alternative rich text editor
3. **Add Testing**: Implement comprehensive test suite
4. **Database Migration**: Move to PostgreSQL for production
5. **Security Hardening**: Environment variables, DEBUG=False
6. **Performance Optimization**: Bundle optimization, caching strategy

---

## 📞 Reporting New Issues

If you encounter additional issues:

1. **Check this document** for existing workarounds
2. **Search GitHub issues** for similar problems
3. **Create detailed issue report** with:
   - Environment details (OS, Node.js, Python versions)
   - Steps to reproduce
   - Error messages and logs
   - Expected vs actual behavior

---

**Last Updated**: 2025-07-26  
**Version**: Deployment Configuration Branch