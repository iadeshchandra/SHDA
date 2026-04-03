[app]
title = SHDA Management
package.name = shda
package.domain = org.shda
source.dir = .
version = 1.0

# Added sqlite3 and ensure no spaces between commas
requirements = python3,kivy,requests,reportlab,sqlite3

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
orientation = portrait
android.archs = arm64-v8a
android.accept_sdk_license = True

# Stable API targets for 2026
android.api = 33
android.minapi = 24
android.ndk = 25b
