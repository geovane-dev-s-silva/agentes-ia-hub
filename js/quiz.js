
const questions = [
  {
    question: "Qual dos seguintes eventos marcou o início da primeira grande transição da humanidade?",
    options: ["A descoberta do fogo", "A invenção da roda", "A fundação de Roma", "O desenvolvimento da agricultura e pecuária"],
    answer: 3
  },
  {
    question: "Qual é uma tecnologia NÃO relacionada à Indústria 4.0?",
    options: ["Biotecnologia", "Inteligência artificial", "Robótica", "Internet das coisas (IoT)"],
    answer: 0
  },
  {
    question: "Qual a principal diferença entre dados e informação?",
    options: ["O dado é um fato bruto, enquanto a informação é o dado contextualizado e com significado.", "O dado é sempre numérico, enquanto a informação pode ser textual.", "A informação é mais importante que o dado para as empresas.", "O dado é obtido através de sensores, enquanto a informação é obtida por meio de pesquisas."],
    answer: 0
  }
];

const quizContainer = document.getElementById('quiz-container');

questions.forEach((q, i) => {
  const div = document.createElement('div');
  div.classList.add('question');
  div.innerHTML = `<p><strong>${i + 1}. ${q.question}</strong></p>` +
    q.options.map((opt, j) => `
      <label>
        <input type="radio" name="q${i}" value="${j}"> ${opt}
      </label><br>
    `).join('');
  quizContainer.appendChild(div);
});

function checkAnswers() {
  let score = 0;
  questions.forEach((q, i) => {
    const selected = document.querySelector(`input[name=q${i}]:checked`);
    if (selected && parseInt(selected.value) === q.answer) {
      score++;
    }
  });
  const result = document.getElementById('result');
  result.innerHTML = `<h3>Você acertou ${score} de ${questions.length} perguntas.</h3>`;
}
