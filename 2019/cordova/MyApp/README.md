# How to install Cordova

must already have [Node.js](http://nodejs.org)
```
npm install -g cordova
```

# how to add / run browser

```
cordova platform add browser
```

for live update
```
cordova plugin add cordova-plugin-browsersync
cordova run browser -- --live-reload

or

cordova run -- --live-reload --ignore=lib/**/*.*
```