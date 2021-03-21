/*
___App States Config___
0 -SERVER_WOKEUP
1 -COMPONENTS_INIT
2 -COMPONENTS_CHANGING
3 -MODEL_SUBMITTING
4 -STRING_CHECKING
5 -SESSION_DESTROYING
*/

const lifeCycleInterval = 100;

// api urls
const indexUrl = "https://fa-python-backend.herokuapp.com";

var app = {
  state: "000000", // initial app state
};

/*
... App basics related methods
*/

// sleep method for app
async function sleep(duration) {
  await new Promise((done) => setTimeout(() => done(), duration));
}

// change the state of app
function change(s, r) {
  app.state = app.state.substring(0, s) + r + app.state.substring(s + 1);
}

// set init loading bar progress
function setInitLoadingProgress(value) {
  $("#init-progress-bar")
    .attr("aria-valuenow", value)
    .css("width", value + "%");
}

// wake up the server
async function serverWakeUp() {
  let getResult = null;
  try {
    getResult = await $.get(indexUrl);
  } catch (error) {
    getResult = await $.get(indexUrl);
  } finally {
    if (getResult.status == "success") {
      setInitLoadingProgress(50 + Math.round(Math.random() * 6) * 5); // 50% - 75%
      change(1, 1);
    }
  }
}

/*
... Tool bar component
*/

/*
... Action bar component
*/

/*
... Canvas component
*/

/*
... Display component
*/

/*
... App lifecycle
*/

(async function lifeCycle() {
  switch (app.state) {
    case "000000":
      // initial ui setup
      $(function () {
        $("#master-div").show().addClass("loaded");
        $("#init-progress").fadeIn();
        $("#init-progress-label").fadeIn();
        setInitLoadingProgress(30); // 30%
      });
      app.state = "100000";
      break;
    case "100000":
      // server sleeps
      await serverWakeUp();
      break;
    case "110000":
      // server woke up
      // comps init
      setInitLoadingProgress(100); // 100%
      app.state = "111000";
      break;
    case "111000":
      // comps initialized
      await sleep(1000);
      $("#init-progress").fadeOut();
      $("#init-progress-label").fadeOut();
      $("#init-progress").parent().hide();
      $("#main-content").fadeIn();
      app.state = "1111110";
      break;
    case "1111110":
      console.log("before done");
      app.state = "1111111";
      break;
    default:
      break;
  }

  if (app.state != "1111111") {
    // console.log("Hello");
    setTimeout(() => lifeCycle(), lifeCycleInterval);
  }
})();
