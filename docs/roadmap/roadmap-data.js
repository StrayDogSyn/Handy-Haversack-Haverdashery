// Feature data for the interactive roadmap
const features = {
    phase2: [
        {
            name: "Initiative Tracker System",
            priority: "high",
            time: "6-8 hours",
            type: "backend",
            assignee: "StrayDogSyn",
            dependencies: ["Character API"],
            description: "Real-time combat turn tracking with HP management and turn order",
            tasks: [
                "Create initiative database model with SQLAlchemy",
                "Implement turn order sorting algorithm",
                "Build API endpoints for combat management",
                "Add HP tracking during combat"
            ],
            apis: ["FastAPI", "SQLAlchemy"],
            files: ["backend/app/models/initiative.py", "backend/app/api/initiative.py"]
        },
        {
            name: "Character Sheet UI Component",
            priority: "high",
            time: "10-12 hours",
            type: "frontend",
            assignee: "GrumbleBee",
            dependencies: ["Character API"],
            description: "Comprehensive character sheet with tabs for skills, feats, and inventory",
            tasks: [
                "Create character sheet layout with Tailwind CSS",
                "Implement ability score calculator",
                "Add skill proficiency management UI",
                "Build inventory management interface"
            ],
            apis: ["React", "Axios"],
            files: ["frontend/src/components/CharacterSheet.tsx"]
        },
        {
            name: "Spell Database & Browser",
            priority: "high",
            time: "8-10 hours",
            type: "backend",
            assignee: "StrayDogSyn",
            dependencies: [],
            description: "Searchable spell database with filtering, favorites, and spell slots",
            tasks: [
                "Create spell database model",
                "Seed database with 200+ Pathfinder 2e spells",
                "Implement search and filter API endpoints",
                "Add spell preparation tracking"
            ],
            apis: ["SQLAlchemy", "Archives of Nethys"],
            files: ["backend/app/models/spell.py", "backend/app/api/spells.py"]
        },
        {
            name: "Campaign Management",
            priority: "medium",
            time: "12-14 hours",
            type: "backend",
            assignee: "StrayDogSyn",
            dependencies: ["Character API"],
            description: "Track campaigns, sessions, party composition, and XP progression",
            tasks: [
                "Create campaign and session models",
                "Implement party management",
                "Add session notes and XP tracking",
                "Build timeline and milestone system"
            ],
            apis: ["SQLAlchemy"],
            files: ["backend/app/models/campaign.py", "backend/app/api/campaigns.py"]
        },
        {
            name: "Navigation & Routing",
            priority: "high",
            time: "4-6 hours",
            type: "frontend",
            assignee: "GrumbleBee",
            dependencies: [],
            description: "Multi-page navigation with React Router",
            tasks: [
                "Install and configure React Router",
                "Create route structure",
                "Build navigation menu component",
                "Add breadcrumb navigation"
            ],
            apis: ["React Router"],
            files: ["frontend/src/router.tsx", "frontend/src/components/Navigation.tsx"]
        },
        {
            name: "Offline Mode (PWA)",
            priority: "medium",
            time: "6-8 hours",
            type: "frontend",
            assignee: "GrumbleBee",
            dependencies: [],
            description: "Progressive Web App with offline capabilities for travel",
            tasks: [
                "Add service worker for caching",
                "Implement IndexedDB for local storage",
                "Create sync mechanism",
                "Add install prompt for mobile"
            ],
            apis: ["Service Workers", "IndexedDB"],
            files: ["frontend/public/sw.js", "frontend/src/utils/offline.ts"]
        }
    ],
    phase3: [
        {
            name: "Real-time Multiplayer",
            priority: "high",
            time: "16-20 hours",
            type: "fullstack",
            assignee: "Both",
            dependencies: ["Initiative Tracker", "Authentication"],
            description: "Share combat tracker and character sheets in real-time with party",
            tasks: [
                "Implement WebSocket server with Socket.IO",
                "Create room/session management",
                "Add permission system (GM vs Players)",
                "Build real-time sync for all game data"
            ],
            apis: ["Socket.IO", "Redis"],
            files: ["backend/app/websocket.py", "frontend/src/services/socket.ts"]
        },
        {
            name: "Virtual Tabletop",
            priority: "high",
            time: "20-24 hours",
            type: "frontend",
            assignee: "GrumbleBee",
            dependencies: ["Real-time Multiplayer"],
            description: "Basic VTT with tokens, grid, and fog of war",
            tasks: [
                "Create canvas-based map renderer",
                "Implement token placement and movement",
                "Add fog of war system",
                "Integrate with combat tracker"
            ],
            apis: ["Canvas API", "Fabric.js"],
            files: ["frontend/src/components/VirtualTabletop.tsx"]
        },
        {
            name: "AI Game Master Assistant",
            priority: "medium",
            time: "16-20 hours",
            type: "backend",
            assignee: "StrayDogSyn",
            dependencies: [],
            description: "AI-powered encounter suggestions, NPC dialogue, and plot hooks",
            tasks: [
                "Integrate Claude API for NPC dialogue",
                "Create encounter suggestion engine",
                "Build plot hook generator",
                "Add campaign consistency checker"
            ],
            apis: ["Anthropic API", "OpenAI API"],
            files: ["backend/app/services/ai_assistant.py"]
        },
        {
            name: "PDF Rulebook Parser",
            priority: "low",
            time: "10-12 hours",
            type: "backend",
            assignee: "StrayDogSyn",
            dependencies: [],
            description: "Extract monsters and spells from PDF rulebooks",
            tasks: [
                "Implement PDF text extraction",
                "Parse stat blocks with regex patterns",
                "Map to database schema",
                "Add validation and error handling"
            ],
            apis: ["pypdf", "pdfplumber"],
            files: ["backend/app/services/pdf_parser.py"]
        },
        {
            name: "Mobile App (React Native)",
            priority: "medium",
            time: "40-50 hours",
            type: "frontend",
            assignee: "GrumbleBee",
            dependencies: ["Offline Mode"],
            description: "Native mobile app for iOS and Android",
            tasks: [
                "Set up React Native with Expo",
                "Port core components to mobile",
                "Implement native features (camera, notifications)",
                "Optimize for mobile UX"
            ],
            apis: ["React Native", "Expo"],
            files: ["mobile/"]
        },
        {
            name: "Voice Commands",
            priority: "low",
            time: "8-10 hours",
            type: "frontend",
            assignee: "GrumbleBee",
            dependencies: [],
            description: "Voice-activated dice rolling and game commands",
            tasks: [
                "Implement Web Speech API",
                "Create command parser",
                "Add voice feedback",
                "Support multiple languages"
            ],
            apis: ["Web Speech API"],
            files: ["frontend/src/services/voice.ts"]
        }
    ]
};

const apiIntegrations = [
    {
        name: "Archives of Nethys",
        status: "Ready",
        url: "https://2e.aonprd.com/",
        description: "Official Pathfinder 2e reference - spell and monster data",
        endpoints: ["spells", "monsters", "items", "feats"],
        implementation: "Web scraping or community API wrappers available"
    },
    {
        name: "Foundry VTT",
        status: "Planned",
        url: "https://foundryvtt.com/",
        description: "Virtual tabletop - character import/export compatibility",
        endpoints: ["characters", "compendiums", "world-data"],
        implementation: "JSON export/import, possible module integration"
    },
    {
        name: "Anthropic Claude",
        status: "Available",
        url: "https://anthropic.com/",
        description: "AI assistant for NPC dialogue and story suggestions",
        endpoints: ["messages"],
        implementation: "Direct API integration (SDK available)"
    },
    {
        name: "Spotify Web API",
        status: "Ready",
        url: "https://developer.spotify.com/",
        description: "Background music and atmospheric playlists",
        endpoints: ["playlists", "tracks", "playback"],
        implementation: "OAuth 2.0 + REST API"
    },
    {
        name: "Pixels Dice",
        status: "Ready",
        url: "https://gamewithpixels.com/",
        description: "Bluetooth-enabled electronic dice integration",
        endpoints: ["bluetooth"],
        implementation: "Web Bluetooth API"
    },
    {
        name: "Roll20 Character Vault",
        status: "Planned",
        url: "https://roll20.net/",
        description: "Character sheet import/export compatibility",
        endpoints: ["characters"],
        implementation: "JSON format import/export"
    },
    {
        name: "D&D Beyond (Adapter)",
        status: "Research",
        url: "https://dndbeyond.com/",
        description: "Character import adapter for D&D 5e to PF2e conversion",
        endpoints: ["characters"],
        implementation: "Third-party API or web scraping"
    },
    {
        name: "Paizo Marketplace",
        status: "Research",
        url: "https://paizo.com/",
        description: "Official Pathfinder content marketplace integration",
        endpoints: ["products", "purchases"],
        implementation: "OAuth if available, web scraping as fallback"
    }
];

const quickWins = [
    { name: "Add d3, d100 support to dice roller", time: "2 hours", type: "backend" },
    { name: "Create dark mode toggle", time: "3 hours", type: "frontend" },
    { name: "Add keyboard shortcuts (R=roll, N=next)", time: "4 hours", type: "frontend" },
    { name: "Implement roll history export to CSV", time: "2 hours", type: "backend" },
    { name: "Add HP bar visualization", time: "3 hours", type: "frontend" },
    { name: "Create encounter difficulty calculator", time: "4 hours", type: "backend" },
    { name: "Add dice roll sound effects", time: "2 hours", type: "frontend" },
    { name: "Implement character quick stats widget", time: "3 hours", type: "frontend" }
];

// Rendering functions
function renderFeatureItem(feature) {
    const item = document.createElement('li');
    item.className = 'feature-item';
    item.dataset.type = feature.type;
    item.dataset.priority = feature.priority;
    
    item.innerHTML = `
        <div class="feature-header">
            <span class="feature-name">${feature.name}</span>
            <div class="feature-meta">
                <span class="priority priority-${feature.priority}">${feature.priority.toUpperCase()}</span>
                <span class="time-estimate">⏱️ ${feature.time}</span>
            </div>
        </div>
        <div class="feature-details">
            <div class="detail-section">
                <h4>📝 Description</h4>
                <p style="color: #cbd5e1;">${feature.description}</p>
            </div>
            <div class="detail-section">
                <h4>👤 Assigned To</h4>
                <span class="dependency-badge">${feature.assignee}</span>
            </div>
            <div class="detail-section">
                <h4>✅ Tasks</h4>
                <ul>
                    ${feature.tasks.map(task => `<li>${task}</li>`).join('')}
                </ul>
            </div>
            ${feature.dependencies.length > 0 ? `
                <div class="detail-section">
                    <h4>🔗 Dependencies</h4>
                    ${feature.dependencies.map(dep => `<span class="dependency-badge">${dep}</span>`).join('')}
                </div>
            ` : ''}
            ${feature.apis && feature.apis.length > 0 ? `
                <div class="detail-section">
                    <h4>🔌 APIs/Libraries</h4>
                    ${feature.apis.map(api => `<span class="dependency-badge">${api}</span>`).join('')}
                </div>
            ` : ''}
            ${feature.files ? `
                <div class="detail-section">
                    <h4>📁 Files to Create</h4>
                    ${feature.files.map(file => `<div class="code-snippet">${file}</div>`).join('')}
                </div>
            ` : ''}
        </div>
    `;
    
    item.addEventListener('click', function() {
        const details = this.querySelector('.feature-details');
        details.classList.toggle('expanded');
        this.classList.toggle('expanded');
    });
    
    return item;
}

function renderPhaseFeatures(phase, containerId) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';
    
    features[phase].forEach(feature => {
        container.appendChild(renderFeatureItem(feature));
    });
}

function renderAPIIntegrations() {
    const container = document.getElementById('apiIntegrations');
    container.innerHTML = '';
    
    apiIntegrations.forEach(api => {
        const card = document.createElement('div');
        card.className = 'integration-card';
        card.innerHTML = `
            <div class="integration-header">
                <div class="integration-name">${api.name}</div>
                <span class="integration-status" style="background: ${
                    api.status === 'Ready' ? '#166534' : 
                    api.status === 'Available' ? '#ca8a04' : 
                    api.status === 'Planned' ? '#1e40af' : '#475569'
                }; color: ${
                    api.status === 'Ready' ? '#86efac' : 
                    api.status === 'Available' ? '#fef3c7' : 
                    api.status === 'Planned' ? '#bfdbfe' : '#e2e8f0'
                };">${api.status}</span>
            </div>
            <p style="color: #cbd5e1; margin-bottom: 15px;">${api.description}</p>
            <div class="detail-section">
                <h4>🔗 URL</h4>
                <a href="${api.url}" target="_blank" style="color: #67e8f9; text-decoration: none;">${api.url}</a>
            </div>
            <div class="detail-section">
                <h4>📡 Endpoints</h4>
                ${api.endpoints.map(endpoint => `<span class="dependency-badge">${endpoint}</span>`).join('')}
            </div>
            <div class="api-integration">
                <h4>💡 Implementation</h4>
                <p style="color: #cbd5e1;">${api.implementation}</p>
            </div>
        `;
        container.appendChild(card);
    });
}

function renderSprint() {
    const container = document.getElementById('sprint1');
    container.innerHTML = '';
    
    // Sprint 1: Top priority features
    const sprint1Features = [
        features.phase2[0], // Initiative Tracker
        features.phase2[1], // Character Sheet
        features.phase2[4]  // Navigation
    ];
    
    sprint1Features.forEach(feature => {
        const card = document.createElement('div');
        card.style.background = '#0f172a';
        card.style.padding = '15px';
        card.style.borderRadius = '8px';
        card.style.marginBottom = '15px';
        card.style.borderLeft = '4px solid #7f1d1d';
        card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <strong style="color: #fbbf24; font-size: 1.1em;">${feature.name}</strong>
                <span class="priority priority-${feature.priority}">${feature.priority}</span>
            </div>
            <p style="color: #94a3b8; font-size: 0.9em; margin-bottom: 10px;">${feature.description}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #64748b; font-size: 0.85em;">⏱️ ${feature.time}</span>
                <span style="color: #67e8f9; font-size: 0.85em;">👤 ${feature.assignee}</span>
            </div>
        `;
        container.appendChild(card);
    });
}

function renderQuickWins() {
    const container = document.getElementById('quickWins');
    container.innerHTML = '';
    
    quickWins.forEach(win => {
        const item = document.createElement('div');
        item.style.background = '#0f172a';
        item.style.padding = '12px 15px';
        item.style.marginBottom = '8px';
        item.style.borderRadius = '6px';
        item.style.borderLeft = '3px solid #0891b2';
        item.style.display = 'flex';
        item.style.justifyContent = 'space-between';
        item.style.alignItems = 'center';
        item.innerHTML = `
            <span style="color: #cbd5e1;">
                <span style="color: #67e8f9;">✨</span>
                ${win.name}
            </span>
            <div>
                <span style="color: #94a3b8; font-size: 0.85em; margin-right: 10px;">${win.time}</span>
                <span class="dependency-badge" style="font-size: 0.75em;">${win.type}</span>
            </div>
        `;
        container.appendChild(item);
    });
}

function initializeRoadmap() {
    renderPhaseFeatures('phase2', 'phase2Features');
    renderPhaseFeatures('phase3', 'phase3Features');
    renderAPIIntegrations();
    renderSprint();
    renderQuickWins();
}
