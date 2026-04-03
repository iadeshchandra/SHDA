[app]
title = SHDA Management
package.name = shda
package.domain = org.shda
source.dir = .
version = 1.0

# Added sqlite3 and openssl for your database and sync
requirements = python3,kivy,requests,reportlab,sqlite3,openssl

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
orientation = portrait

# Stability settings for 2026
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
