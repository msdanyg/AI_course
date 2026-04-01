var API = null;
var findAPITries = 0;
var scormInitialized = false;

function findAPI(win) {
    while ((win.API == null) && (win.parent != null) && (win.parent != win)) {
        findAPITries++;
        if (findAPITries > 500) {
            console.log("Cannot find SCORM API - reached max attempts");
            return null;
        }
        win = win.parent;
    }
    return win.API;
}

function getAPI() {
    var theAPI = findAPI(window);
    if ((theAPI == null) && (window.opener != null) && (typeof(window.opener) != "undefined")) {
        theAPI = findAPI(window.opener);
    }
    if (theAPI == null) {
        console.log("Unable to find SCORM API adapter");
    } else {
        console.log("SCORM API found successfully");
    }
    return theAPI;
}

function initializeSCORM() {
    API = getAPI();
    if (API != null) {
        var result = API.LMSInitialize("");
        console.log("LMSInitialize result: " + result);

        if (result == "true") {
            scormInitialized = true;

            var status = API.LMSGetValue("cmi.core.lesson_status");
            console.log("Current lesson status: " + status);

            if (status == "not attempted" || status == "") {
                API.LMSSetValue("cmi.core.lesson_status", "incomplete");
                API.LMSCommit("");
            }
            return true;
        }
    }
    return false;
}

function setSCORMValue(key, value) {
    if (API != null && scormInitialized) {
        var result = API.LMSSetValue(key, value);
        console.log("Set " + key + " = " + value + " : " + result);
        return result == "true";
    }
    return false;
}

function getSCORMValue(key) {
    if (API != null && scormInitialized) {
        var value = API.LMSGetValue(key);
        console.log("Get " + key + " = " + value);
        return value;
    }
    return "";
}

function setSCORMStatus(status) {
    if (setSCORMValue("cmi.core.lesson_status", status)) {
        API.LMSCommit("");
        console.log("Status committed: " + status);
    }
}

function setSCORMScore(score) {
    if (API != null && scormInitialized) {
        setSCORMValue("cmi.core.score.raw", score.toString());
        setSCORMValue("cmi.core.score.min", "0");
        setSCORMValue("cmi.core.score.max", "100");
        API.LMSCommit("");
        console.log("Score committed: " + score);
    }
}

function setSCORMPassed(passed) {
    var status = passed ? "passed" : "failed";
    setSCORMStatus(status);
}

function finishSCORM() {
    if (API != null && scormInitialized) {
        var commitResult = API.LMSCommit("");
        console.log("Final commit: " + commitResult);

        var finishResult = API.LMSFinish("");
        console.log("LMSFinish: " + finishResult);
    }
}

window.addEventListener('load', function() {
    console.log("Page loaded - initializing SCORM");
    initializeSCORM();
});

window.addEventListener('beforeunload', function() {
    console.log("Page unloading - finishing SCORM");
    finishSCORM();
});
