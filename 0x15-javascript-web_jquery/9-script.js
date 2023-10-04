$(document).ready(function () {
  $.get("https://fourtonfish.com/hellosalut/?lang=fr", function (data) {
    // Set the translation of hello to the DIV#hello element
    $("DIV#hello").text(data.hello);
  });
});
