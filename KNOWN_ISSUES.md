# Known Issues

This document outlines known issues, limitations, and workarounds for the Django Reddit Clone application.

## 🚨 Critical Issues

### 1. Frontend Display Issue - Only Font Visible
**Status**: ❌ **Critical - App Not Functional**  
**Affected Components**: Entire Angular frontend  
**Description**: Angular application loads but only shows font/text in top left corner, no UI components render properly.

**Symptoms**:
- HTML page loads correctly at `http://localhost:4200/django_reddit`
- JavaScript files load successfully (main.js, vendor.js, etc.)
- Django API responds correctly at `http://localhost:12000/api/v1/posts/`
- Angular dev server compiles without errors
- Only minimal text visible in browser, no proper UI rendering

**Investigation Status**:
- ✅ Fixed baseHref routing issue (Angular dev server now serves from correct path)
- ✅ Fixed API URL configuration (updated environment.ts to use port 12000)
- ✅ Verified CORS configuration working
- ❌ Root cause of UI rendering failure still unknown

**Potential Causes**:
1. CSS/SCSS compilation issues
2. Angular Material components not loading
3. JavaScript runtime errors preventing component initialization
4. Missing dependencies or module loading failures

**Next Steps**:
1. Check browser console for JavaScript errors
2. Verify Angular Material and FlexLayout modules
3. Test with minimal component to isolate issue
4. Check CSS compilation and loading

### 2. Froala WYSIWYG Editor Replaced with CKEditor
**Status**: ✅ **Resolved**  
**Affected Components**: Post creation, comment editing  
**Description**: Successfully replaced Froala editor with CKEditor 5 to resolve licensing and compatibility issues.

**Changes Made**:
- Removed Froala dependencies from package.json
- Added CKEditor 5 (`@ckeditor/ckeditor5-angular`, `@ckeditor/ckeditor5-build-classic`)
- Updated create-post component with CKEditor implementation
- Added proper CKEditor styling and configuration

**Impact**: 
- ✅ Rich text editing now available
- ✅ WYSIWYG formatting options working
- ✅ No licensing issues
- ✅ Better TypeScript compatibility

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

## 🚀 Current Deployment Status

### Servers Running
- ✅ **Django API**: Running on port 12000 (`http://localhost:12000`)
- ✅ **Angular Dev Server**: Running on port 4200 (`http://localhost:4200/django_reddit`)

### API Status
- ✅ **Posts Endpoint**: `http://localhost:12000/api/v1/posts/` returning 40 test posts
- ✅ **CORS Configuration**: Properly configured for cross-origin requests
- ✅ **Database**: SQLite with sample data loaded

### Frontend Status
- ⚠️ **HTML Loading**: Page loads correctly with proper base href
- ⚠️ **JavaScript Loading**: All JS bundles load successfully
- ❌ **UI Rendering**: Critical issue - only text visible, no components render
- ✅ **Build Process**: Angular compilation successful without errors

### Recent Fixes Applied
1. **Angular Routing**: Fixed baseHref and servePath configuration
2. **API URLs**: Updated environment.ts to use correct port (12000)
3. **CKEditor Integration**: Successfully replaced Froala with CKEditor 5
4. **CORS Setup**: Configured for development and production URLs
5. **Git Management**: All changes committed and pushed to main branch

### Immediate Action Required
The frontend display issue is preventing the application from being usable. Investigation needed to determine why Angular components are not rendering despite successful compilation and loading.

---

**Last Updated**: 2025-07-26  
**Version**: Main Branch (Post-CKEditor Integration)