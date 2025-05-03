// Easter Egg: Mensagem divertida no console
console.log('Eu sou Grok, criado por xAI. "A vida, o universo e tudo mais" começa aqui! 🚀');

// Espera o DOM carregar completamente antes de executar
document.addEventListener('DOMContentLoaded', () => {
  // Verifica se estamos em arquivos.html (que tem o elemento fileList)
  if (document.getElementById('fileList')) {
    // Lista de arquivos (edite aqui para adicionar ou remover arquivos)
    const files = [
      { name: 'Introdução LLM', author: 'Celso Azevedo', type: 'PDF', url: 'https://drive.google.com/file/d/1Z6Ee41REZBwb1KMFr9qqs8Z3XZGzm0O4/view' },
      { name: 'Gestão de Projetos de IA', author: 'Arthur Castro', type: 'PDF', url: 'https://drive.google.com/file/d/1jaDh3pwVaGU7bxkh7LDuek78PH8p0b0o/view' },
      { name: 'Abertura', author: 'Celso Azevedo', type: 'PDF', url: 'https://drive.google.com/file/d/1JPhZxNWYYcyoEX6wFEkZv2GvtvzQwlYF/view' },
      { name: 'Respostas das dúvidas até 2025-04-12', author: 'Admin', type: 'PDF', url: 'https://drive.google.com/file/d/127Ftc4qFvQ_kNujEQIshLSJYCfvud9Cd/view' },
      { name: 'Meta - IA em prol do humano', author: 'Admin', type: 'Vídeo', url: 'https://drive.google.com/file/d/15ioRbBS1OoHapBIx2m-1jCB91At7dFvS/view' },
      { name: 'Sobre o Curso - I2A2', author: 'Admin', type: 'PDF', url: 'https://drive.google.com/file/d/1XpElYxof7MbqQH8oTSRo2HFCQgemGTlN/view' }
    ];

    // Elementos do DOM
    const fileList = document.getElementById('fileList');
    const searchInput = document.getElementById('search');

    // Função para renderizar a lista de arquivos
    function renderFiles(filter = '') {
      // Limpa a lista atual
      fileList.innerHTML = '';
      // Filtra arquivos por nome ou autor e adiciona ao DOM
      files
        .filter(file => 
          file.name.toLowerCase().includes(filter.toLowerCase()) || 
          file.author.toLowerCase().includes(filter.toLowerCase())
        )
        .forEach(file => {
          fileList.innerHTML += `<li><i class="fas fa-${file.type === 'PDF' ? 'file-pdf' : 'video'}"></i> <a href="${file.url}" target="_blank">${file.name} - ${file.author}</a></li>`;
        });
    }

    // Renderiza a lista inicial
    renderFiles();

    // Atualiza a lista conforme o usuário digita no campo de busca
    searchInput.addEventListener('input', (e) => renderFiles(e.target.value));
  }
});