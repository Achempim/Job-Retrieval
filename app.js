// Fetch job data from SQLite using Flask API (or JSON)
function buildMetadata(jobId) {
  d3.json("/api/jobs/" + jobId).then((data) => {
    let metadataPanel = d3.select("#sample-metadata");
    metadataPanel.html("");
    Object.entries(data).forEach(([key, value]) => {
      metadataPanel.append("h6").text(`${key.toUpperCase()}: ${value}`);
    });
  });
}

// Build charts for job data
function buildCharts() {
  d3.json("/api/jobs").then((data) => {
    let topJobs = data.slice(0, 10);
    let yticks = topJobs.map(job => job.title).reverse();

    // Bar Chart
    let barTrace = {
      x: topJobs.map(job => job.salary).reverse(),
      y: yticks,
      text: topJobs.map(job => job.company).reverse(),
      type: "bar",
      orientation: "h"
    };

    let barLayout = { title: "Top 10 Jobs by Salary" };
    Plotly.newPlot("bar", [barTrace], barLayout);

    // Bubble Chart
    let bubbleTrace = {
      x: data.map(job => job.salary),
      y: data.map(job => job.id),
      text: data.map(job => job.company),
      mode: 'markers',
      marker: { size: data.map(job => job.salary), color: data.map(job => job.id) }
    };

    let bubbleLayout = { title: "Job Bubble Chart", xaxis: { title: "Salary" } };
    Plotly.newPlot("bubble", [bubbleTrace], bubbleLayout);
  });
}

// Initialize dashboard
function init() {
  buildCharts();
}

init();
