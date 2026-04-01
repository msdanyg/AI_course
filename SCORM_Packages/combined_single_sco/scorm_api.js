/**
 * SCORM 1.2 API Wrapper for Articulate Reach 360
 * Solo Pilot to Squadron Leader Training Course
 */

var API = null;
var findAPITries = 0;
var scormInitialized = false;

// Find the SCORM API in window hierarchy
function findAPI(win) {
    while ((win.API == null) && (win.parent != null) && (win.parent != win)) {
        findAPITries++;
        if (findAPITries > 500) {
            console.log("SCORM: Cannot find API - reached max attempts");
            return null;
        }
        win = win.parent;
    }
    return win.API;
}

// Get API from window or opener
function getAPI() {
    var theAPI = findAPI(window);
    if ((theAPI == null) && (window.opener != null) && (typeof(window.opener) != "undefined")) {
        theAPI = findAPI(window.opener);
    }
    if (theAPI == null) {
        console.log("SCORM: Unable to find API adapter - running in standalone mode");
    } else {
        console.log("SCORM: API found successfully");
    }
    return theAPI;
}

// Initialize SCORM session
function initializeSCORM() {
    API = getAPI();
    if (API != null) {
        var result = API.LMSInitialize("");
        console.log("SCORM: LMSInitialize result: " + result);

        if (result == "true") {
            scormInitialized = true;

            var status = API.LMSGetValue("cmi.core.lesson_status");
            console.log("SCORM: Current lesson status: " + status);

            if (status == "not attempted" || status == "") {
                API.LMSSetValue("cmi.core.lesson_status", "incomplete");
                API.LMSCommit("");
                console.log("SCORM: Status set to incomplete");
            }
            return true;
        }
    }
    return false;
}

// Set SCORM data value
function setSCORMValue(key, value) {
    if (API != null && scormInitialized) {
        var result = API.LMSSetValue(key, value);
        console.log("SCORM: Set " + key + " = " + value + " : " + result);
        return result == "true";
    }
    console.log("SCORM: Cannot set value - not initialized");
    return false;
}

// Get SCORM data value
function getSCORMValue(key) {
    if (API != null && scormInitialized) {
        var value = API.LMSGetValue(key);
        console.log("SCORM: Get " + key + " = " + value);
        return value;
    }
    return "";
}

// Set lesson status
function setSCORMStatus(status) {
    if (setSCORMValue("cmi.core.lesson_status", status)) {
        API.LMSCommit("");
        console.log("SCORM: Status committed: " + status);
    }
}

// Set score (0-100)
function setSCORMScore(score) {
    if (API != null && scormInitialized) {
        setSCORMValue("cmi.core.score.raw", score.toString());
        setSCORMValue("cmi.core.score.min", "0");
        setSCORMValue("cmi.core.score.max", "100");
        API.LMSCommit("");
        console.log("SCORM: Score committed: " + score);
    } else {
        console.log("SCORM: Score set (standalone): " + score);
    }
}

// Set passed/failed status
function setSCORMPassed(passed) {
    var status = passed ? "passed" : "failed";
    setSCORMStatus(status);
}

// Set completion percentage (0-100)
function setSCORMProgress(percent) {
    if (API != null && scormInitialized) {
        // SCORM 1.2 uses cmi.core.lesson_location for bookmarking
        setSCORMValue("cmi.core.lesson_location", percent.toString());
        API.LMSCommit("");
    }
}

// Finish SCORM session
function finishSCORM() {
    if (API != null && scormInitialized) {
        var commitResult = API.LMSCommit("");
        console.log("SCORM: Final commit: " + commitResult);

        var finishResult = API.LMSFinish("");
        console.log("SCORM: LMSFinish: " + finishResult);
    }
}

// Initialize on page load
window.addEventListener('load', function() {
    console.log("SCORM: Page loaded - initializing");
    initializeSCORM();
});

// Finish on page unload
window.addEventListener('beforeunload', function() {
    console.log("SCORM: Page unloading - finishing session");
    finishSCORM();
});

// Utility: Complete the course
function completeCourse(score, passed) {
    if (score !== undefined) {
        setSCORMScore(score);
    }
    if (passed !== undefined) {
        setSCORMPassed(passed);
    } else {
        setSCORMStatus("completed");
    }
    console.log("SCORM: Course completed");
}
