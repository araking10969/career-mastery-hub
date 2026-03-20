// Load state from localStorage or use defaults
const savedState = JSON.parse(localStorage.getItem('career_hub_state'));
const state = savedState || {
    currentView: 'dashboard',
    user: { name: 'ゆうや', streak: 12, targetDate: '2026-05-01' },
    timer: { secondsRemaining: 1500, isActive: false, interval: null },
    companies: []
};

const elements = {
    navItems: document.querySelectorAll('.nav-item'),
    views: document.querySelectorAll('.content-view'),
    timerDisplay: document.querySelector('.timer-display'),
    startBtn: document.getElementById('start-btn'),
    kanbanColumns: {
        interested: document.getElementById('col-interested'),
        applying: document.getElementById('col-applying'),
        interview: document.getElementById('col-interview'),
        offer: document.getElementById('col-offer')
    },
    // Modal elements
    addCompanyBtn: document.getElementById('add-company-btn'),
    modalContainer: document.getElementById('modal-container'),
    closeModalBtn: document.getElementById('close-modal-btn'),
    cancelBtn: document.getElementById('cancel-btn'),
    addCompanyForm: document.getElementById('add-company-form')
};

function saveState() {
    localStorage.setItem('career_hub_state', JSON.stringify({
        ...state,
        timer: { ...state.timer, isActive: false, interval: null } // Don't save active timer
    }));
}

function switchView(viewName) {
    state.currentView = viewName;
    elements.navItems.forEach(item => item.classList.toggle('active', item.dataset.view === viewName));
    elements.views.forEach(view => view.classList.toggle('hidden', view.id !== viewName));
    if (viewName === 'kanban') renderKanban();
}

// Kanban Functions
function renderKanban() {
    Object.entries(elements.kanbanColumns).forEach(([key, col]) => {
        const cardsCont = col.querySelector('.kanban-cards');
        if (!cardsCont) return;
        cardsCont.innerHTML = '';
        
        const filtered = state.companies.filter(c => c.status === key);
        col.querySelector('.count').textContent = filtered.length;
        
        filtered.forEach(company => {
            const card = document.createElement('div');
            card.className = 'kanban-card';
            card.draggable = true;
            card.dataset.id = company.id;
            
            card.addEventListener('dragstart', (e) => {
                // Ignore drag if clicking inside textarea
                if (e.target.tagName === 'TEXTAREA') {
                    e.preventDefault();
                    return;
                }
                e.dataTransfer.setData('text/plain', company.id);
                e.dataTransfer.effectAllowed = 'move';
                setTimeout(() => card.classList.add('dragging'), 0);
            });
            
            card.addEventListener('dragend', () => {
                card.classList.remove('dragging');
            });
            
            card.innerHTML = `
                <h5>${company.name}</h5>
                <p>${company.job}</p>
                <textarea class="card-memo" placeholder="メモを入力..." oninput="updateNote('${company.id}', this.value)">${company.notes || ''}</textarea>
                <div class="card-actions">
                    <button class="secondary-button mini-btn" onclick="deleteCompany('${company.id}')">削除</button>
                </div>
            `;
            cardsCont.appendChild(card);
        });
    });
}

window.updateNote = (id, value) => {
    const company = state.companies.find(c => c.id === id);
    if (company) {
        company.notes = value;
        saveState();
    }
};

function initKanbanEvents() {
    Object.entries(elements.kanbanColumns).forEach(([key, col]) => {
        col.addEventListener('dragover', (e) => {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            col.classList.add('dragover');
        });

        col.addEventListener('dragleave', () => {
            col.classList.remove('dragover');
        });

        col.addEventListener('drop', (e) => {
            e.preventDefault();
            col.classList.remove('dragover');
            const id = e.dataTransfer.getData('text/plain');
            const company = state.companies.find(c => c.id === id);
            if (company && company.status !== key) {
                company.status = key;
                saveState();
                renderKanban();
            }
        });
    });
}

window.moveCompany = (id, direction) => {
    const company = state.companies.find(c => c.id === id);
    const statuses = ['interested', 'applying', 'interview', 'offer'];
    const currentIdx = statuses.indexOf(company.status);
    if (direction === 'next' && currentIdx < statuses.length - 1) {
        company.status = statuses[currentIdx + 1];
    }
    saveState();
    renderKanban();
};

window.deleteCompany = (id) => {
    state.companies = state.companies.filter(c => c.id !== id);
    saveState();
    renderKanban();
};

// Modal Functions
function toggleModal(show) {
    elements.modalContainer.classList.toggle('hidden', !show);
}

// Timer Functions
function updateTimerDisplay() {
    const min = Math.floor(state.timer.secondsRemaining / 60);
    const sec = state.timer.secondsRemaining % 60;
    elements.timerDisplay.textContent = `${String(min).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;
}

function toggleTimer() {
    if (state.timer.isActive) {
        clearInterval(state.timer.interval);
        state.timer.isActive = false;
        elements.startBtn.textContent = 'スタート';
    } else {
        state.timer.isActive = true;
        elements.startBtn.textContent = '一時停止';
        state.timer.interval = setInterval(() => {
            if (state.timer.secondsRemaining > 0) {
                state.timer.secondsRemaining--;
                updateTimerDisplay();
            } else {
                clearInterval(state.timer.interval);
                state.timer.isActive = false;
                elements.startBtn.textContent = '終了';
            }
        }, 1000);
    }
}

function init() {
    elements.navItems.forEach(item => item.addEventListener('click', () => switchView(item.dataset.view)));
    if (elements.startBtn) elements.startBtn.addEventListener('click', toggleTimer);
    
    // Modal events
    if (elements.addCompanyBtn) elements.addCompanyBtn.addEventListener('click', () => toggleModal(true));
    if (elements.closeModalBtn) elements.closeModalBtn.addEventListener('click', () => toggleModal(false));
    if (elements.cancelBtn) elements.cancelBtn.addEventListener('click', () => toggleModal(false));
    
    // Form event
    if (elements.addCompanyForm) {
        elements.addCompanyForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const newCompany = {
                id: Date.now().toString(),
                name: document.getElementById('company-name').value,
                job: document.getElementById('job-title').value,
                status: document.getElementById('initial-status').value,
                notes: ""
            };
            state.companies.push(newCompany);
            saveState();
            toggleModal(false);
            renderKanban();
            elements.addCompanyForm.reset();
        });
    }

    initKanbanEvents();
    switchView(state.currentView || 'dashboard');
    updateTimerDisplay();
    lucide.createIcons();
}

// Prompt templates
const prompts = {
    'self-pr': '以下の私の経歴と実績をもとに、応募企業の求める人物像に合致する「自己PR」を、構成案とともに3パターン作成してください。\n\n[実績]\n・...',
    'interview': '私は今、大手テック企業のエンジニア職の面接を控えています。私の経歴をもとに、想定される難しい質問を5つ挙げ、それに対する回答のポイントを論理的に整理してください。\n\n[経歴]\n・...',
    'company': '以下の企業の募集要項とWebサイト情報をもとに、中期経営計画に紐づく私のポジションへの期待値と、逆質問で聞くべき内容を3つ挙げてください。\n\n[企業名]\n...',
    'email': '面接後の丁寧なお礼メールを作成してください。面接で印象に残った話題として「エンジニアの成長環境」について触れたいと考えています。'
};

let toastTimer = null;

window.copyPrompt = (id) => {
    const text = prompts[id];
    const toast = document.getElementById('copy-toast');
    const content = document.getElementById('copy-content');
    
    // Copy to clipboard
    navigator.clipboard.writeText(text).then(() => {
        // Show feedback
        content.textContent = text;
        toast.classList.remove('hidden');
        
        // Auto hide after 5 seconds
        if (toastTimer) clearTimeout(toastTimer);
        toastTimer = setTimeout(() => {
            toast.classList.add('hidden');
        }, 5000);
    });
};

document.addEventListener('DOMContentLoaded', init);
