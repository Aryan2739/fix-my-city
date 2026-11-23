// Fix My City — Application State & Interactive Engine

// Initial Mock Dataset for Civic Complaints (Ramdeobaba University Campus & Vicinity, Nagpur)
const INITIAL_COMPLAINTS = [
  {
    id: "FMC-101",
    category: "roads",
    categoryLabel: "Roads & Potholes",
    categoryIcon: "bi-cone-striped",
    title: "Deep Hazardous Pothole near Main Entrance Gate",
    description: "Large asphalt crater right outside the main college entrance on Katol Road. Student two-wheelers and college buses are swerving into oncoming traffic to avoid it.",
    address: "Main Gate, Ramdeobaba University, Katol Road, Nagpur",
    lat: 21.1772,
    lng: 79.0610,
    severity: "urgent",
    status: "open",
    reportedBy: "Aman Sharma (CSE Dept)",
    reportedTime: "2 hours ago",
    upvotes: 48,
    department: "Nagpur Municipal Corporation (NMC) - PWD",
    officer: "Pending Assignment",
    image: "assets/pothole.jpg",
    history: [
      { step: 1, name: "Complaint Registered", date: "Today, 09:15 AM", done: true },
      { step: 2, name: "Under Municipal Verification", date: "Today, 10:30 AM", done: true },
      { step: 3, name: "Crew Dispatched", date: "In Queue", done: false },
      { step: 4, name: "Resolved & Closed", date: "Pending", done: false }
    ]
  },
  {
    id: "FMC-102",
    category: "lighting",
    categoryLabel: "Street Lighting",
    categoryIcon: "bi-lightbulb-off-fill",
    title: "Series of 4 Dark Streetlights on Campus Hostel Pathway",
    description: "Pedestrian walkway between the RBU Boys' Hostel and Tech Park has been completely dark for 3 nights. Poses a security and safety concern for evening students.",
    address: "Hostel & Temple Pathway, Ramdeo Tekdi, RBU, Nagpur",
    lat: 21.1755,
    lng: 79.0625,
    severity: "high",
    status: "in-progress",
    reportedBy: "Priya Deshmukh (Hostel Council)",
    reportedTime: "Yesterday",
    upvotes: 35,
    department: "MSEDCL & NMC Electrical Works",
    officer: "Junior Engineer K. B. Patil (Dharampeth Zone)",
    image: "assets/streetlight.jpg",
    history: [
      { step: 1, name: "Complaint Registered", date: "Yesterday, 07:45 PM", done: true },
      { step: 2, name: "Under Municipal Verification", date: "Yesterday, 09:10 PM", done: true },
      { step: 3, name: "Crew Dispatched", date: "Today, 08:00 AM — Crew Inspecting Transformer", done: true },
      { step: 4, name: "Resolved & Closed", date: "Scheduled completion by 4 PM", done: false }
    ]
  },
  {
    id: "FMC-103",
    category: "waste",
    categoryLabel: "Waste Management",
    categoryIcon: "bi-trash3-fill",
    title: "Overflowing Garbage Bins outside Campus Gate 2",
    description: "Commercial bins overflowing onto the walkway opposite Gate 2. Stray animals scattering plastic waste across the Katol Road footpath.",
    address: "Opposite Gate 2, Gittikhadan, Katol Road, Nagpur",
    lat: 21.1780,
    lng: 79.0602,
    severity: "medium",
    status: "resolved",
    reportedBy: "Rohan Kulkarni (Student)",
    reportedTime: "2 days ago",
    upvotes: 72,
    department: "NMC Solid Waste & Sanitation",
    officer: "Health Inspector Sunil Gawande",
    image: "assets/garbage.jpg",
    resolvedImage: "assets/street_cleaned.jpg",
    history: [
      { step: 1, name: "Complaint Registered", date: "Nov 21, 11:20 AM", done: true },
      { step: 2, name: "Under Municipal Verification", date: "Nov 21, 01:15 PM", done: true },
      { step: 3, name: "Crew Dispatched", date: "Nov 22, 06:30 AM — Sanitation Truck #14", done: true },
      { step: 4, name: "Resolved & Closed", date: "Nov 22, 10:45 AM — Cleared & Bleaching powder applied", done: true }
    ]
  },
  {
    id: "FMC-104",
    category: "water",
    categoryLabel: "Water & Drainage",
    categoryIcon: "bi-droplet-half",
    title: "Drinking Water Supply Pipeline Leak near Sports Complex",
    description: "Treated municipal water pipe burst near the university cricket ground boundary, creating heavy waterlogging on the connecting lane.",
    address: "Sports Complex Road, Ramdeobaba University, Nagpur",
    lat: 21.1748,
    lng: 79.0632,
    severity: "urgent",
    status: "in-progress",
    reportedBy: "Coach Vikram Rathod",
    reportedTime: "5 hours ago",
    upvotes: 61,
    department: "Orange City Water (OCW) & NMC Water Works",
    officer: "Rapid Response Unit West Zone",
    image: "assets/water_leak.jpg",
    history: [
      { step: 1, name: "Complaint Registered", date: "Today, 06:10 AM", done: true },
      { step: 2, name: "Under Municipal Verification", date: "Today, 07:00 AM", done: true },
      { step: 3, name: "Crew Dispatched", date: "Today, 08:30 AM — Valve replacement underway", done: true },
      { step: 4, name: "Resolved & Closed", date: "Estimated 2 hours remaining", done: false }
    ]
  }
];

// In-memory application state
let complaints = INITIAL_COMPLAINTS;
try {
  // Clear any old cache so the user sees the 4 real photos immediately
  localStorage.clear();
} catch (e) {
  console.log("Storage reset complete");
}
let currentFilterCategory = "all";
let currentFilterStatus = "all";
let searchQuery = "";
let currentViewMode = "grid"; // 'grid' or 'map'
let activeReportCategory = "roads";
let uploadedImageDataUrl = null;
let leafletMap = null;
let mapMarkers = [];

// DOM Elements Initialization
document.addEventListener("DOMContentLoaded", () => {
  initApp();
  initEventListeners();
  renderStats();
  renderComplaints();
  initLeafletMap();
  populateAdminTable();
  trackTicket("FMC-102"); // default loaded ticket in tracker
});

function initApp() {
  console.log("Fix My City Civic Web App & Prototype Engine Initialized.");
}

// -------------------------------------------------------------
// Stats Calculation & Display
// -------------------------------------------------------------
function renderStats() {
  const total = complaints.length;
  const resolved = complaints.filter(c => c.status === "resolved").length;
  const inProgress = complaints.filter(c => c.status === "in-progress").length;
  const open = complaints.filter(c => c.status === "open").length;

  document.getElementById("statTotal").textContent = total;
  document.getElementById("statResolved").textContent = resolved;
  document.getElementById("statInProgress").textContent = inProgress;
  document.getElementById("statOpen").textContent = open;
  
  const resolutionRate = total > 0 ? Math.round((resolved / total) * 100) : 0;
  const badgeEl = document.getElementById("resolutionRateBadge");
  if (badgeEl) badgeEl.textContent = `${resolutionRate}% Resolution Rate`;
}

// -------------------------------------------------------------
// Feed Rendering & Filtering
// -------------------------------------------------------------
function getFilteredComplaints() {
  return complaints.filter(c => {
    const matchesCategory = currentFilterCategory === "all" || c.category === currentFilterCategory;
    const matchesStatus = currentFilterStatus === "all" || c.status === currentFilterStatus;
    const matchesSearch = searchQuery === "" || 
      c.title.toLowerCase().includes(searchQuery) ||
      c.description.toLowerCase().includes(searchQuery) ||
      c.address.toLowerCase().includes(searchQuery) ||
      c.id.toLowerCase().includes(searchQuery);
    return matchesCategory && matchesStatus && matchesSearch;
  });
}

function renderComplaints() {
  const container = document.getElementById("complaintsGrid");
  const filtered = getFilteredComplaints();
  const countEl = document.getElementById("filterResultCount");
  if (countEl) countEl.textContent = `${filtered.length} complaints shown`;

  if (!container) return;
  container.innerHTML = "";

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="col-12 text-center py-5">
        <i class="bi bi-search display-4 text-muted mb-3 d-block"></i>
        <h5 class="fw-semibold text-secondary">No complaints match your criteria</h5>
        <p class="text-muted small">Try selecting "All Categories" or clearing the search bar.</p>
        <button class="btn btn-outline-teal btn-sm" onclick="resetFilters()">Reset All Filters</button>
      </div>
    `;
    return;
  }

  filtered.forEach(c => {
    const statusClass = c.status === "resolved" ? "resolved" : (c.status === "in-progress" ? "in-progress" : "open");
    const statusLabel = c.status === "resolved" ? "Resolved" : (c.status === "in-progress" ? "In Progress" : "Reported");

    const col = document.createElement("div");
    col.className = "col-lg-6 col-md-6 mb-4";
    col.innerHTML = `
      <div class="issue-card">
        <div class="position-relative">
          <img src="${c.image}" alt="${c.title}" class="issue-thumbnail">
          <span class="position-absolute top-0 start-0 m-2 status-badge ${statusClass}">
            <span class="status-dot"></span> ${statusLabel}
          </span>
          <span class="position-absolute top-0 end-0 m-2 badge bg-dark bg-opacity-75 font-monospace">
            #${c.id}
          </span>
        </div>
        <div class="p-3 d-flex flex-column flex-grow-1">
          <div class="d-flex align-items-center gap-2 mb-2">
            <span class="badge bg-light text-dark border">
              <i class="bi ${c.categoryIcon} text-teal me-1"></i>${c.categoryLabel}
            </span>
            <span class="text-muted small ms-auto"><i class="bi bi-clock me-1"></i>${c.reportedTime}</span>
          </div>
          
          <h5 class="h6 fw-bold text-dark mb-1">${c.title}</h5>
          <p class="text-muted small flex-grow-1 mb-2 line-clamp-2">${c.description}</p>
          
          <div class="small text-secondary mb-3">
            <i class="bi bi-geo-alt-fill text-danger me-1"></i>${c.address}
          </div>

          <div class="pt-2 border-top d-flex align-items-center justify-content-between mt-auto">
            <button class="btn-upvote" onclick="handleUpvote('${c.id}', this)">
              <i class="bi bi-hand-thumbs-up"></i>
              <span>${c.upvotes}</span>
            </button>
            <div class="d-flex gap-2">
              <button class="btn btn-sm btn-outline-secondary" onclick="viewComplaintDetails('${c.id}')" title="Inspect">
                Details
              </button>
              <button class="btn btn-sm btn-teal" onclick="trackTicket('${c.id}')" title="Track Live Status">
                Track <i class="bi bi-arrow-right"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    `;
    container.appendChild(col);
  });

  updateMapMarkers(filtered);
}

// -------------------------------------------------------------
// Interactive Leaflet Map
// -------------------------------------------------------------
function initLeafletMap() {
  const mapEl = document.getElementById("mapContainer");
  if (!mapEl) return;

  // Center around Shri Ramdeobaba University (RBU) campus, Katol Road, Nagpur
  leafletMap = L.map("mapContainer").setView([21.1764, 79.0617], 15);

  // Free OpenStreetMap tile layer
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; OpenStreetMap contributors | Fix My City — Ramdeobaba University'
  }).addTo(leafletMap);

  updateMapMarkers(getFilteredComplaints());
}

function updateMapMarkers(items) {
  if (!leafletMap) return;

  // Clear existing markers
  mapMarkers.forEach(m => leafletMap.removeLayer(m));
  mapMarkers = [];

  items.forEach(c => {
    const pinColor = c.status === "resolved" ? "#10B981" : (c.status === "in-progress" ? "#F59E0B" : "#EF4444");

    const customIcon = L.divIcon({
      className: "custom-map-pin",
      html: `
        <div style="background-color: ${pinColor}; width: 30px; height: 30px; border-radius: 50% 50% 50% 0; transform: rotate(-45deg); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(0,0,0,0.3); border: 2px solid #fff;">
          <i class="bi ${c.categoryIcon}" style="transform: rotate(45deg); color: #fff; font-size: 14px;"></i>
        </div>
      `,
      iconSize: [30, 30],
      iconAnchor: [15, 30]
    });

    const marker = L.marker([c.lat, c.lng], { icon: customIcon }).addTo(leafletMap);
    
    marker.bindPopup(`
      <div style="font-family: Inter, sans-serif; min-width: 200px;">
        <span class="badge" style="background-color: ${pinColor}; color: #fff; font-size: 11px;">${c.status.toUpperCase()}</span>
        <h6 style="margin: 6px 0 3px; font-weight: 700; font-size: 13px;">${c.title}</h6>
        <p style="margin: 0 0 6px; font-size: 11px; color: #64748B;">${c.address}</p>
        <button onclick="trackTicket('${c.id}')" style="background: #0D9488; color: #fff; border: none; padding: 4px 10px; border-radius: 6px; font-size: 11px; cursor: pointer; width: 100%;">
          View Resolution Progress
        </button>
      </div>
    `);

    mapMarkers.push(marker);
  });
}

// -------------------------------------------------------------
// Upvote Mechanism
// -------------------------------------------------------------
function handleUpvote(id, buttonEl) {
  const item = complaints.find(c => c.id === id);
  if (!item) return;

  if (buttonEl.classList.contains("voted")) {
    item.upvotes -= 1;
    buttonEl.classList.remove("voted");
  } else {
    item.upvotes += 1;
    buttonEl.classList.add("voted");
  }

  buttonEl.querySelector("span").textContent = item.upvotes;
  saveComplaintsToStorage();
}

// -------------------------------------------------------------
// Ticket Lifecycle Tracker
// -------------------------------------------------------------
function trackTicket(ticketId) {
  // Normalize ID
  const cleanId = ticketId.replace("#", "").trim().toUpperCase();
  const ticket = complaints.find(c => c.id.toUpperCase() === cleanId);
  const targetSection = document.getElementById("trackerSection");

  if (targetSection) {
    targetSection.scrollIntoView({ behavior: "smooth" });
  }

  const resultContainer = document.getElementById("trackerResultCard");
  const inputEl = document.getElementById("ticketSearchInput");
  if (inputEl) inputEl.value = cleanId;

  if (!ticket) {
    resultContainer.innerHTML = `
      <div class="alert alert-warning d-flex align-items-center gap-3">
        <i class="bi bi-exclamation-triangle-fill fs-3 text-warning"></i>
        <div>
          <h6 class="alert-heading fw-bold mb-0">Ticket Not Found</h6>
          <p class="mb-0 small">No civic report registered with ID <strong>#${cleanId}</strong>. Please check your reference code or pick one of the sample tickets below.</p>
        </div>
      </div>
    `;
    return;
  }

  // Build Stepper Timeline HTML
  const steps = [
    { title: "Complaint Registered", desc: "Citizen uploaded report with geo-coordinates and photo evidence.", time: ticket.history[0]?.date || "Nov 23, 08:00 AM" },
    { title: "Municipal Triage & Review", desc: "Assigned priority level and routed to responsible civic agency.", time: ticket.history[1]?.date || "Pending" },
    { title: "Field Crew Dispatched", desc: `Assigned: ${ticket.department} (${ticket.officer})`, time: ticket.history[2]?.date || "Pending" },
    { title: "Resolved & Citizen Verified", desc: "Physical work concluded, QA photo verified, closed.", time: ticket.history[3]?.date || "Pending" }
  ];

  let completedStepsCount = 1;
  if (ticket.status === "in-progress") completedStepsCount = 3;
  if (ticket.status === "resolved") completedStepsCount = 4;

  let stepperHtml = "";
  steps.forEach((s, idx) => {
    const stepNumber = idx + 1;
    let stateClass = "";
    let icon = stepNumber;

    if (stepNumber < completedStepsCount || (ticket.status === "resolved" && stepNumber <= 4)) {
      stateClass = "completed";
      icon = '<i class="bi bi-check-lg"></i>';
    } else if (stepNumber === completedStepsCount) {
      stateClass = "active";
      icon = `<span class="spinner-grow spinner-grow-sm text-teal" role="status"></span>`;
    }

    stepperHtml += `
      <div class="step-item ${stateClass}">
        <div class="step-circle">${icon}</div>
        <div class="step-title">${s.title}</div>
        <div class="step-time text-muted small mt-1">${s.time}</div>
      </div>
    `;
  });

  // Before & After container for resolved items
  let beforeAfterHtml = "";
  if (ticket.status === "resolved" && ticket.resolvedImage) {
    beforeAfterHtml = `
      <div class="mt-4 pt-3 border-top">
        <h6 class="fw-bold mb-3"><i class="bi bi-images text-teal me-2"></i>Official Work Verification Proof (Before vs After)</h6>
        <div class="comparison-container">
          <div class="comparison-box">
            <span class="comparison-label before">Before (Citizen Report)</span>
            <img src="${ticket.image}" alt="Before Issue">
          </div>
          <div class="comparison-box">
            <span class="comparison-label after">After (Crew Resolved)</span>
            <img src="${ticket.resolvedImage}" alt="After Resolved">
          </div>
        </div>
      </div>
    `;
  }

  resultContainer.innerHTML = `
    <div class="card border-0 shadow-sm p-4 rounded-4 bg-white">
      <div class="d-flex flex-wrap align-items-center justify-content-between gap-3 border-bottom pb-3">
        <div>
          <span class="badge bg-teal-subtle text-teal fw-bold font-monospace px-3 py-1 fs-6 mb-2">#${ticket.id}</span>
          <h4 class="fw-bold mb-1">${ticket.title}</h4>
          <p class="text-muted small mb-0"><i class="bi bi-geo-alt-fill text-danger me-1"></i>${ticket.address}</p>
        </div>
        <div class="text-end">
          <span class="badge rounded-pill ${ticket.status === 'resolved' ? 'bg-success' : (ticket.status === 'in-progress' ? 'bg-warning text-dark' : 'bg-danger')} px-3 py-2 fs-6">
            ${ticket.status.toUpperCase()}
          </span>
          <div class="text-muted small mt-1">Severity: <span class="fw-bold text-capitalize">${ticket.severity}</span></div>
        </div>
      </div>

      <!-- Stepper component modeled from Figma Frame 4 -->
      <div class="tracking-stepper">
        ${stepperHtml}
      </div>

      <div class="row g-3 bg-light p-3 rounded-3 mt-2">
        <div class="col-md-4">
          <span class="text-muted small d-block">Managing Department</span>
          <span class="fw-bold text-dark"><i class="bi bi-building me-1 text-teal"></i>${ticket.department}</span>
        </div>
        <div class="col-md-4">
          <span class="text-muted small d-block">Assigned Field Unit / Officer</span>
          <span class="fw-bold text-dark"><i class="bi bi-person-badge me-1 text-teal"></i>${ticket.officer}</span>
        </div>
        <div class="col-md-4">
          <span class="text-muted small d-block">Reported By</span>
          <span class="fw-bold text-dark"><i class="bi bi-shield-check me-1 text-teal"></i>${ticket.reportedBy}</span>
        </div>
      </div>

      ${beforeAfterHtml}
    </div>
  `;
}

// -------------------------------------------------------------
// Issue Submission Modal Logic
// -------------------------------------------------------------
function selectCategory(categoryKey, cardEl) {
  activeReportCategory = categoryKey;
  document.querySelectorAll(".category-select-card").forEach(c => c.classList.remove("selected"));
  cardEl.classList.add("selected");
}

function handleImageUpload(input) {
  const preview = document.getElementById("imagePreview");
  const placeholder = document.getElementById("uploadPlaceholder");
  
  if (input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = function(e) {
      preview.src = e.target.result;
      preview.classList.remove("d-none");
      placeholder.classList.add("d-none");
      uploadedImageDataUrl = e.target.result;
    };
    reader.readAsDataURL(input.files[0]);
  }
}

function simulateGeoLocation() {
  const locInput = document.getElementById("issueLocationInput");
  const btn = document.getElementById("btnDetectLoc");
  
  btn.innerHTML = `<span class="spinner-border spinner-border-sm me-1"></span> Acquired GPS...`;
  
  setTimeout(() => {
    locInput.value = "Shri Ramdeobaba University (RBU), Ramdeo Tekdi, Katol Road, Nagpur (GPS: 21.1764° N, 79.0617° E)";
    btn.innerHTML = `<i class="bi bi-check-circle-fill text-success me-1"></i> RBU Location Locked`;
    btn.classList.replace("btn-outline-teal", "btn-light");
  }, 700);
}

function submitNewComplaint(event) {
  event.preventDefault();

  const title = document.getElementById("issueTitleInput").value.trim();
  const description = document.getElementById("issueDescInput").value.trim();
  const address = document.getElementById("issueLocationInput").value.trim() || "Reported Location, Ward 2";
  const severity = document.getElementById("issueSeveritySelect").value;
  const citizenName = document.getElementById("citizenNameInput").value.trim() || "Civic Citizen";

  const categoryMap = {
    roads: { label: "Roads & Potholes", icon: "bi-cone-striped", dept: "Public Works & Transportation" },
    waste: { label: "Waste Management", icon: "bi-trash3-fill", dept: "Solid Waste & Sanitation" },
    lighting: { label: "Street Lighting", icon: "bi-lightbulb-off-fill", dept: "Municipal Power & Lighting" },
    water: { label: "Water & Drainage", icon: "bi-droplet-half", dept: "Department of Water & Sewage" },
    greenery: { label: "Parks & Greenery", icon: "bi-tree-fill", dept: "Parks & Urban Forestry" },
    traffic: { label: "Traffic & Signals", icon: "bi-stoplights-fill", dept: "Traffic Operations Command" }
  };

  const selectedCategoryInfo = categoryMap[activeReportCategory] || categoryMap.roads;
  const newTicketId = `FMC-${Math.floor(1000 + Math.random() * 9000)}`;

  // Default fallback image if user did not upload one (using real civic images)
  const fallbackImages = {
    roads: "assets/pothole.jpg",
    waste: "assets/garbage.jpg",
    lighting: "assets/streetlight.jpg",
    water: "assets/water_leak.jpg",
    greenery: "assets/tree_fallen.jpg",
    traffic: "assets/traffic_light.jpg"
  };

  const newTicket = {
    id: newTicketId,
    category: activeReportCategory,
    categoryLabel: selectedCategoryInfo.label,
    categoryIcon: selectedCategoryInfo.icon,
    title: title,
    description: description,
    address: address,
    lat: 21.1764 + (Math.random() - 0.5) * 0.008,
    lng: 79.0617 + (Math.random() - 0.5) * 0.008,
    severity: severity,
    status: "open",
    reportedBy: citizenName,
    reportedTime: "Just now",
    upvotes: 1,
    department: selectedCategoryInfo.dept,
    officer: "Pending Assignment",
    image: uploadedImageDataUrl || fallbackImages[activeReportCategory],
    history: [
      { step: 1, name: "Complaint Registered", date: "Just now", done: true },
      { step: 2, name: "Under Municipal Verification", date: "Queued for Review", done: false },
      { step: 3, name: "Crew Dispatched", date: "Pending", done: false },
      { step: 4, name: "Resolved & Closed", date: "Pending", done: false }
    ]
  };

  // Add to top of list
  complaints.unshift(newTicket);
  saveComplaintsToStorage();

  // Reset form
  document.getElementById("reportIssueForm").reset();
  uploadedImageDataUrl = null;
  document.getElementById("imagePreview").classList.add("d-none");
  document.getElementById("uploadPlaceholder").classList.remove("d-none");

  // Close report modal
  const reportModal = bootstrap.Modal.getInstance(document.getElementById("reportIssueModal"));
  if (reportModal) reportModal.hide();

  // Update UI components
  renderStats();
  renderComplaints();
  populateAdminTable();

  // Show Success Modal
  document.getElementById("newTicketGeneratedId").textContent = `#${newTicketId}`;
  document.getElementById("btnModalTrack").onclick = () => {
    const successModal = bootstrap.Modal.getInstance(document.getElementById("successModal"));
    if (successModal) successModal.hide();
    trackTicket(newTicketId);
  };

  const successModal = new bootstrap.Modal(document.getElementById("successModal"));
  successModal.show();
}

// -------------------------------------------------------------
// Municipal / Public Service Authority Dashboard (Admin)
// -------------------------------------------------------------
function populateAdminTable() {
  const tableBody = document.getElementById("adminTableBody");
  if (!tableBody) return;

  tableBody.innerHTML = "";
  complaints.forEach(c => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td class="fw-bold font-monospace">#${c.id}</td>
      <td>
        <span class="badge bg-light text-dark border">
          <i class="bi ${c.categoryIcon} me-1"></i>${c.categoryLabel}
        </span>
      </td>
      <td>
        <div class="fw-semibold text-truncate" style="max-width: 200px;">${c.title}</div>
        <div class="text-muted small">${c.address}</div>
      </td>
      <td><span class="dept-pill">${c.department}</span></td>
      <td>
        <span class="badge ${c.severity === 'urgent' ? 'bg-danger' : (c.severity === 'high' ? 'bg-warning text-dark' : 'bg-info text-dark')}">
          ${c.severity.toUpperCase()}
        </span>
      </td>
      <td>
        <select class="form-select form-select-sm" onchange="updateTicketStatus('${c.id}', this.value)">
          <option value="open" ${c.status === 'open' ? 'selected' : ''}>Reported (Open)</option>
          <option value="in-progress" ${c.status === 'in-progress' ? 'selected' : ''}>In Progress</option>
          <option value="resolved" ${c.status === 'resolved' ? 'selected' : ''}>Resolved & Closed</option>
        </select>
      </td>
      <td>
        <button class="btn btn-sm btn-outline-teal" onclick="trackTicket('${c.id}')">Inspect</button>
      </td>
    `;
    tableBody.appendChild(tr);
  });
}

function updateTicketStatus(id, newStatus) {
  const ticket = complaints.find(c => c.id === id);
  if (!ticket) return;

  ticket.status = newStatus;

  if (newStatus === "in-progress") {
    ticket.officer = "Assigned Rapid Response Unit";
    ticket.history[1].done = true;
    ticket.history[2].done = true;
    ticket.history[2].date = "Dispatched by Authority Admin";
  } else if (newStatus === "resolved") {
    ticket.history[1].done = true;
    ticket.history[2].done = true;
    ticket.history[3].done = true;
    ticket.history[3].date = "Verified Resolved by Authority Admin";
    if (!ticket.resolvedImage) {
      ticket.resolvedImage = "https://images.unsplash.com/photo-1584467735871-8e85353a8413?auto=format&fit=crop&w=600&q=80";
    }
  }

  saveComplaintsToStorage();
  renderStats();
  renderComplaints();
  trackTicket(id);
}

// -------------------------------------------------------------
// Detailed Modal View
// -------------------------------------------------------------
function viewComplaintDetails(id) {
  const ticket = complaints.find(c => c.id === id);
  if (!ticket) return;

  const content = document.getElementById("complaintDetailsContent");
  content.innerHTML = `
    <div class="row g-3">
      <div class="col-md-6">
        <img src="${ticket.image}" alt="${ticket.title}" class="img-fluid rounded-3 mb-2" style="max-height: 250px; width: 100%; object-fit: cover;">
        ${ticket.resolvedImage ? `
          <div class="mt-2">
            <span class="badge bg-success mb-1">Resolution Evidence Photo</span>
            <img src="${ticket.resolvedImage}" alt="Resolved" class="img-fluid rounded-3" style="max-height: 200px; width: 100%; object-fit: cover;">
          </div>
        ` : ''}
      </div>
      <div class="col-md-6">
        <span class="badge bg-dark font-monospace mb-2">Ticket #${ticket.id}</span>
        <h5 class="fw-bold">${ticket.title}</h5>
        <p class="text-muted small">${ticket.description}</p>
        
        <ul class="list-group list-group-flush small">
          <li class="list-group-item px-0 d-flex justify-content-between">
            <span class="text-muted">Category:</span>
            <span class="fw-bold">${ticket.categoryLabel}</span>
          </li>
          <li class="list-group-item px-0 d-flex justify-content-between">
            <span class="text-muted">Location:</span>
            <span class="fw-bold text-end">${ticket.address}</span>
          </li>
          <li class="list-group-item px-0 d-flex justify-content-between">
            <span class="text-muted">Managing Authority:</span>
            <span class="fw-bold text-teal">${ticket.department}</span>
          </li>
          <li class="list-group-item px-0 d-flex justify-content-between">
            <span class="text-muted">Current Status:</span>
            <span class="badge ${ticket.status === 'resolved' ? 'bg-success' : (ticket.status === 'in-progress' ? 'bg-warning text-dark' : 'bg-danger')}">${ticket.status.toUpperCase()}</span>
          </li>
          <li class="list-group-item px-0 d-flex justify-content-between">
            <span class="text-muted">Citizen Endorsements:</span>
            <span class="fw-bold">${ticket.upvotes} Upvotes</span>
          </li>
        </ul>

        <div class="mt-3">
          <button class="btn btn-teal w-100" onclick="trackTicket('${ticket.id}'); bootstrap.Modal.getInstance(document.getElementById('detailsModal')).hide();">
            <i class="bi bi-clock-history me-1"></i> Open Full Lifecycle Tracker
          </button>
        </div>
      </div>
    </div>
  `;

  const detailsModal = new bootstrap.Modal(document.getElementById("detailsModal"));
  detailsModal.show();
}

// -------------------------------------------------------------
// UI Event Handlers
// -------------------------------------------------------------
function initEventListeners() {
  // Category filter pills
  document.querySelectorAll(".category-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".category-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentFilterCategory = btn.dataset.category;
      renderComplaints();
    });
  });

  // Status dropdown filter
  const statusSelect = document.getElementById("statusFilterSelect");
  if (statusSelect) {
    statusSelect.addEventListener("change", (e) => {
      currentFilterStatus = e.target.value;
      renderComplaints();
    });
  }

  // Live search input
  const searchInput = document.getElementById("searchInput");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      renderComplaints();
    });
  }

  // View toggle (Grid vs Map)
  const btnGridView = document.getElementById("btnGridView");
  const btnMapView = document.getElementById("btnMapView");
  const gridSection = document.getElementById("complaintsGridSection");
  const mapSection = document.getElementById("complaintsMapSection");

  if (btnGridView && btnMapView) {
    btnGridView.addEventListener("click", () => {
      btnGridView.classList.add("active");
      btnMapView.classList.remove("active");
      gridSection.classList.remove("d-none");
      mapSection.classList.add("d-none");
    });

    btnMapView.addEventListener("click", () => {
      btnMapView.classList.add("active");
      btnGridView.classList.remove("active");
      mapSection.classList.remove("d-none");
      gridSection.classList.add("d-none");
      setTimeout(() => {
        if (leafletMap) leafletMap.invalidateSize();
      }, 200);
    });
  }
}

function resetFilters() {
  currentFilterCategory = "all";
  currentFilterStatus = "all";
  searchQuery = "";
  
  document.querySelectorAll(".category-btn").forEach(b => {
    if (b.dataset.category === "all") b.classList.add("active");
    else b.classList.remove("active");
  });

  const statusSelect = document.getElementById("statusFilterSelect");
  if (statusSelect) statusSelect.value = "all";

  const searchInput = document.getElementById("searchInput");
  if (searchInput) searchInput.value = "";

  renderComplaints();
}

function saveComplaintsToStorage() {
  try {
    localStorage.setItem("fmc_complaints", JSON.stringify(complaints));
  } catch (err) {
    console.warn("Storage quota exceeded or disabled", err);
  }
}
