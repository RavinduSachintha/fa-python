const indexUrl = "https://fa-python-backend.herokuapp.com";
var pageState = "sleep";

async function initialize() {
  let tries = 3;
  while (pageState == "sleep" || tries > 0) {
    let getResult = await $.get(indexUrl).then();
    if (getResult.status == "success") {
      pageState = "wokeup";
    }
    tries--;
  }
}

async function indicatePageState() {
  if (pageState == "sleep") {
    $("#sleep-indicator").show();
    $("#main-content").hide();
  } else if (pageState == "wokeup") {
    $("#sleep-indicator").hide();
    $("#main-content").show();
  } else {
    $("#sleep-indicator").text("Something went wrong");
  }
}

async function main() {
  await initialize();
  await indicatePageState();
}

main();
