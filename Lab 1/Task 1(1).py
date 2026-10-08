# AI Milestones Timeline
# Historical evidence task

timeline = [
    {
        "year": "1950",
        "event": "Turing Test proposed",
        "significance": "Alan Turing proposed a conversational test for considering whether a machine can imitate human-like responses.",
        "source": "Turing, A. M. (1950), Computing Machinery and Intelligence"
    },
    {
        "year": "1956",
        "event": "Dartmouth Workshop",
        "significance": "The Dartmouth project helped establish artificial intelligence as a formal research field.",
        "source": "McCarthy et al. (1955), A Proposal for the Dartmouth Summer Research Project on AI"
    },
    {
        "year": "1974-1980",
        "event": "First AI Winter",
        "significance": "Reduced funding and disappointment in early AI systems led to a major slowdown in AI research.",
        "source": "Russell & Norvig, Artificial Intelligence: A Modern Approach"
    },
    {
        "year": "1997",
        "event": "IBM Deep Blue defeats Garry Kasparov",
        "significance": "Deep Blue's chess victory demonstrated the power of specialized computer systems for difficult search problems.",
        "source": "IBM, Deep Blue"
    },
    {
        "year": "2012",
        "event": "AlexNet and ImageNet",
        "significance": "AlexNet showed that deep neural networks could achieve a major improvement in large-scale image recognition.",
        "source": "Krizhevsky, Sutskever & Hinton (2012), NIPS"
    },
    {
        "year": "2017",
        "event": "Transformer architecture",
        "significance": "The Transformer introduced an attention-based architecture that became highly influential in modern language AI.",
        "source": "Vaswani et al. (2017), Attention Is All You Need"
    }
]

print("AI MILESTONES TIMELINE")
print("=" * 70)

for item in timeline:
    print(f"Year/Period: {item['year']}")
    print(f"Event: {item['event']}")
    print(f"Significance: {item['significance']}")
    print(f"Source: {item['source']}")
    print("-" * 70)
