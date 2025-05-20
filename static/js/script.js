document.addEventListener('DOMContentLoaded', () => {
    // Elementos da interface
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const clearBtn = document.getElementById('clearBtn');
    const saveBtn = document.getElementById('saveBtn');
    const statusElement = document.getElementById('status');
    const transcriptElement = document.getElementById('transcript');
    
    // Verificar suporte à API de reconhecimento de fala
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        statusElement.textContent = 'Seu navegador não suporta reconhecimento de fala. Tente usar o Chrome.';
        startBtn.disabled = true;
        return;
    }
    
    // Inicializar o objeto de reconhecimento de fala
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    
    // Configurar o reconhecimento de fala
    recognition.lang = 'pt-BR';
    recognition.continuous = true;
    recognition.interimResults = true;
    
    // Variáveis de controle
    let isRecording = false;
    let finalTranscript = '';
    let interimTranscript = '';
    
    // Função para iniciar a transcrição
    function startRecording() {
        finalTranscript = transcriptElement.textContent || '';
        interimTranscript = '';
        
        try {
            recognition.start();
            isRecording = true;
            updateUI();
        } catch (error) {
            console.error('Erro ao iniciar o reconhecimento:', error);
            statusElement.textContent = `Erro ao iniciar: ${error.message}`;
        }
    }
    
    // Função para parar a transcrição
    function stopRecording() {
        if (isRecording) {
            recognition.stop();
            isRecording = false;
            updateUI();
        }
    }
    
    // Função para limpar a transcrição
    function clearTranscript() {
        finalTranscript = '';
        interimTranscript = '';
        transcriptElement.textContent = '';
        updateUI();
    }
    
    // Função para salvar a transcrição
    function saveTranscript() {
        const text = transcriptElement.textContent;
        if (!text) {
            statusElement.textContent = 'Nada para salvar.';
            return;
        }
        
        // Salvar localmente como arquivo de texto
        const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `transcricao_${new Date().toISOString().slice(0, 19).replace(/[T:]/g, '-')}.txt`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        
        statusElement.textContent = 'Transcrição salva com sucesso!';
    }
    
    // Função para atualizar a interface
    function updateUI() {
        startBtn.disabled = isRecording;
        stopBtn.disabled = !isRecording;
        
        if (isRecording) {
            statusElement.textContent = 'Gravando... Fale agora.';
            transcriptElement.classList.add('recording');
        } else {
            statusElement.textContent = 'Pronto para iniciar a transcrição';
            transcriptElement.classList.remove('recording');
        }
    }
    
    // Eventos de reconhecimento de fala
    recognition.onresult = (event) => {
        interimTranscript = '';
        
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalTranscript += event.results[i][0].transcript + ' ';
            } else {
                interimTranscript += event.results[i][0].transcript;
            }
        }
        
        // Atualizar o elemento de transcrição
        transcriptElement.textContent = finalTranscript + interimTranscript;
    };
    
    recognition.onerror = (event) => {
        console.error('Erro de reconhecimento:', event.error);
        statusElement.textContent = `Erro: ${event.error}`;
        
        if (event.error === 'not-allowed') {
            statusElement.textContent = 'Permissão de microfone negada. Verifique as configurações do seu navegador.';
        }
        
        isRecording = false;
        updateUI();
    };
    
    recognition.onend = () => {
        if (isRecording) {
            // Se ainda estiver gravando, reinicie o reconhecimento
            // Isso ajuda a manter a gravação contínua
            recognition.start();
        } else {
            statusElement.textContent = 'Transcrição finalizada.';
            updateUI();
        }
    };
    
    // Eventos de clique dos botões
    startBtn.addEventListener('click', startRecording);
    stopBtn.addEventListener('click', stopRecording);
    clearBtn.addEventListener('click', clearTranscript);
    saveBtn.addEventListener('click', saveTranscript);
    
    // Inicializar a interface
    updateUI();
});
