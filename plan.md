# Discord Clone - Improvements Plan

## Critical Issues

- [ ] **Missing schema files** - `app/schemas/user_schemas.py` is imported but appears missing
- [ ] **Empty/unimplemented files** - `deps.py`, `server.py`, `channel.py`, `message.py`, `authStore.ts`, `login.tsx`, etc. are empty
- [ ] **No routers registered** - Only `auth_router` is included in `main.py`. Users, channels, servers, messages routers need to be registered

## Security Improvements

- [ ] **Hardcoded SECRET_KEY** (`backend/app/core/config.py:8`) - Use environment variable only, remove default
- [ ] **No CORS configuration** - Add CORS middleware for frontend origin
- [ ] **No rate limiting** - Protect auth endpoints from brute force
- [ ] **No refresh tokens** - Currently only access tokens with 24h expiry

## Architecture Improvements

- [ ] **Add database migrations** - Use Alembic instead of `Base.metadata.create_all()`
- [ ] **Add error handling middleware** - Global exception handler
- [ ] **Add logging** - No logging currently configured
- [ ] **Add password strength validation** - Function exists in `auth_service.py` but is never called during registration
- [ ] **Add input sanitization** - Validate string inputs for length, special characters

## Frontend Improvements

- [ ] **Implement empty components** - `login.tsx`, `register.tsx`, `authStore.ts` are empty
- [ ] **Add proper state management** - Implement auth state with token storage (localStorage/cookies)
- [ ] **Add HTTP interceptors** - Attach JWT to requests automatically
- [ ] **Add error handling** - User-friendly error messages

## General

- [ ] **Add type safety** - Frontend needs TypeScript types for API responses
- [ ] **Add README** - Documentation for setup and running the project
