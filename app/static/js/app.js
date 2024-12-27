document.getElementById('analyze-button').addEventListener('click', async () => {
    const text = document.getElementById('input-text').value;
    if (!text) {
        alert("Digite uma frase!");
        return;
    }
    
    const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    
    if (!response.ok) {
        alert("Erro ao analisar a frase.");
        return;
    }
    else
        {
         console.log("Resposta", response)   
        }
    
    const data = await response.json();
    const percentages = data.sentiment_percentages;
    
    // Atualizar emoji
    const emojiDiv = document.getElementById('emoji');
    emojiDiv.innerHTML = '';
    if (percentages['positive'] >= 0.5) {
        emojiDiv.innerHTML = '<h1>😀</h1>';
    } else {
        emojiDiv.innerHTML = '<h1>😡</h1>';
    }
    
    // Atualizar gráfico
    const graphDiv = document.getElementById('graph');
    
    // Limpar o gráfico antes de desenhar um novo
    graphDiv.innerHTML = '';  // Isso limpa o conteúdo anterior do gráfico
    
    const trace = {
        x: ['Positive', 'Negative'],
        y: [percentages['positive'],  percentages['negative']],
        type: 'bar'
    };
    
    // Redesenhar o gráfico
    Plotly.newPlot(graphDiv, [trace]);
});