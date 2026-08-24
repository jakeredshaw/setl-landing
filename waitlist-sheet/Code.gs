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

    // Skip duplicates so one person can't pad the list.
    var existing = sh.getLastRow() > 1
      ? sh.getRange(2, 1, sh.getLastRow() - 1, 1).getValues().map(function (r) {
          return String(r[0]).trim().toLowerCase();
        })
      : [];
    if (existing.indexOf(email) !== -1) return out('duplicate');

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

function doGet() {
  return out('SETL waitlist endpoint is live.');
}

function sheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
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
