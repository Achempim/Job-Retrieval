const API_BASE_URL = "http://127.0.0.1:5000";

function fetchJobs() {
    let query = document.getElementById("searchQuery").value;
    if (!query) {
        query = "Data Engineer"; // Default value
    }

    fetch(`${API_BASE_URL}/api/jobs/search?q=${query}`)
    .then(response => response.json())
    .then(data => {
        displayJobs(data);
    })
    .catch(error => console.error("Error fetching jobs:", error));
}

function displayJobs(jobs) {
    let jobListDiv = document.getElementById("job-list");
    jobListDiv.innerHTML = ""; // Clear previous results

    if (jobs.length === 0) {
        jobListDiv.innerHTML = "<p>No jobs found.</p>";
        return;
    }

    let jobHTML = "<ul class='list-group'>";
    jobs.forEach(job => {
        jobHTML += `
            <li class='list-group-item'>
                <h5>${job.title}</h5>
                <p><strong>Company:</strong> ${job.company}</p>
                <p><strong>Location:</strong> ${job.location}</p>
                <p><strong>Salary:</strong> ${job.salary}</p>
                <a href="${job.link}" target="_blank" class="btn btn-primary">View Job</a>
            </li>
        `;
    });
    jobHTML += "</ul>";
    jobListDiv.innerHTML = jobHTML;
}