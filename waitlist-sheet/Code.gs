/**
 * SETL waitlist -> Google Sheet
 *
 * Paste this into Extensions > Apps Script on the spreadsheet that should
 * collect signups, then Deploy > New deployment > Web app:
 *   Execute as:        Me
 *   Who has access:    Anyone
 * Copy the resulting /exec URL into ENDPOINT in index.html.
 */

var SHEET_NAME = 'Waitlist';

// The SETL Waitlist spreadsheet. Hard-coded so this works whether the script is
// bound to the sheet or standalone.
var SHEET_ID = '1HstfyprIWvqdwVI9by7l81WYGI9zGYTl8R4fNVXvTKw';

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var p     = (e && e.parameter) || {};
    var email = String(p.email || '').trim().toLowerCase();

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) {
      return out('invalid');
    }

    var sh = sheet();

    // Every submission is recorded, including repeats from the same address.
    // Deliberately no duplicate check: a rejected repeat looked to the visitor
    // like the form had silently failed.
    sh.appendRow([
      email,
      p.ts || new Date().toISOString(),
      p.source || '',
      (e && e.parameter && e.parameter.ua) || ''
    ]);
    return out('ok');
  } catch (err) {
    return out('error: ' + err);
  } finally {
    lock.releaseLock();
  }
}

function doGet(e) {
  var p = (e && e.parameter) || {};

  // ?action=count -> the real number of rows on the waitlist, as JSON.
  // Used by the sign-up counter on the landing page. Counts data rows only,
  // so the header row is excluded and an empty sheet returns 0.
  if (p.action === 'count') {
    try {
      var rows = Math.max(0, sheet().getLastRow() - 1);
      return json({ count: rows });
    } catch (err) {
      return json({ error: String(err) });
    }
  }

  return out('SETL waitlist endpoint is live.');
}

function json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function sheet() {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sh = ss.getSheetByName(SHEET_NAME);
  if (!sh) {
    sh = ss.insertSheet(SHEET_NAME);
    sh.appendRow(['Email', 'Signed up (UTC)', 'Source', 'Notes']);
    sh.getRange('A1:D1').setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}

function out(msg) {
  return ContentService.createTextOutput(msg).setMimeType(ContentService.MimeType.TEXT);
}
