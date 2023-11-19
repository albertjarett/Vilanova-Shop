let jqueryParams = [];

function jQuery(r) {
  jqueryParams.push(r);
  return jQuery;
}

function $(r) {
  jqueryParams.push(r);
  return $;
}