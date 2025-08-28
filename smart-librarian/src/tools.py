"""
tools.py
Tool: get_summary_by_title(title: str) – returnează rezumatul complet pentru titlul exact.
"""
from typing import Optional

book_summaries_dict = {
    "1984": "Romanul explorează teme precum supravegherea, controlul social și pierderea libertății individuale într-o societate distopică. Winston Smith luptă împotriva unui regim totalitar condus de Big Brother.",
    "The Hobbit": "O poveste fantastică despre curaj, prietenie și aventură. Bilbo Baggins pornește într-o călătorie alături de vrăjitorul Gandalf și o trupă de pitici pentru a recupera o comoară păzită de dragonul Smaug.",
    "Harry Potter 1": "Primul volum din seria Harry Potter urmărește descoperirea lumii magice de către Harry, prietenia cu Ron și Hermione, și lupta împotriva forțelor întunecate la Hogwarts.",
    "Fellowship of the Ring": "Prima parte din trilogia Stăpânul Inelelor. Un grup de eroi pornește într-o misiune pentru a distruge Inelul Puterii, explorând teme precum sacrificiul, prietenia și lupta dintre bine și rău.",
    "To Kill a Mockingbird": "Romanul abordează teme de justiție, rasism și empatie. Scout Finch crește într-un oraș sudist, învățând despre moralitate și prejudecăți prin procesul tatălui său, Atticus.",
    "Pride and Prejudice": "O poveste clasică despre dragoste, mândrie și prejudecăți sociale. Elizabeth Bennet și Mr. Darcy navighează provocările societății engleze din secolul XIX.",
    "The Book Thief": "În timpul celui de-al Doilea Război Mondial, Liesel descoperă puterea cuvintelor și a cărților, în timp ce trăiește într-o Germanie nazistă. Prietenia și pierderea sunt teme centrale.",
    "The Catcher in the Rye": "Holden Caulfield explorează alienarea, inocența și dificultățile maturizării într-o lume pe care o percepe ca fiind falsă.",
    "The Name of the Wind": "Povestea lui Kvothe, un tânăr talentat care devine magician și muzician. Romanul explorează misterul, cunoașterea și supraviețuirea.",
    "The Road": "Un tată și fiul său călătoresc printr-o lume post-apocaliptică, luptând pentru supraviețuire. Temele principale sunt speranța, dragostea paternă și disperarea.",
    "All the Light We Cannot See": "În timpul războiului, destinele unei fete oarbe franceze și ale unui băiat german se intersectează. Romanul explorează umanitatea, supraviețuirea și compasiunea.",
    "The Alchemist": "Santiago pornește într-o călătorie pentru a-și descoperi destinul. Temele centrale sunt visurile, căutarea sensului și transformarea personală."
}

def get_summary_by_title(title: str) -> Optional[str]:
    """
    Returnează rezumatul complet pentru titlul exact.
    :param title: Titlul cărții
    :return: Rezumatul complet sau None dacă nu există
    """
    return book_summaries_dict.get(title)
