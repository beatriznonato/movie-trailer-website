import freshTomatoes
import media

# storing movie information
extraordinario = media.Movie(
    "Extraordinário",
    """Auggie Pullman (Jacob Tremblay) é um garoto que nasceu com uma
    deformação facial, o que fez com que passasse por 27 cirurgias plásticas.
    Aos 10 anos, ele pela primeira vez frequentará uma escola regular, como
    qualquer outra criança. Lá, precisa lidar com a sensação constante de ser
    sempre observado e avaliado por todos à sua volta.""",
    "http://br.web.img3.acsta.net/c_215_290/pictures/17/11/28/18/32/3262971.jpg",  # noqa
    "https://www.youtube.com/watch?v=6g80d7igX0k",
    "1h 51min",
    "Drama, Família"
    )

belezaOculta = media.Movie(
    "Beleza Oculta",
    """Após uma tragédia pessoal, Howard (Will Smith) entra em depressão e
    passa a escrever cartas para a Morte, o Tempo e o Amor - algo que preocupa
    seus amigos. Mas o que parece impossível, se torna realidade quando essas
    três partes do universo decidem responder. Morte (Helen Mirren),
    Tempo (Jacob Latimore) e Amor (Keira Knightley) vão tentar ensinar o valor
    da vida para o protagonista.""",
    "http://br.web.img2.acsta.net/c_215_290/pictures/16/10/13/21/27/038061.jpg",  # noqa
    "https://www.youtube.com/watch?v=fSbMvWW_BBE",
    "1h 37min",
    "Drama"
    )


logan = media.Movie(
    "Logan",
    """Em 2029, Logan (Hugh Jackman) ganha a vida como chofer de limousine
    para cuidar do nonagenário Charles Xavier (Patrick Stewart). Debilitado
    fisicamente e esgotado emocionalmente, ele é procurado por Gabriela
    (Elizabeth Rodriguez), uma mexicana que precisa da ajuda do ex-X-Men para
    defender a pequena Laura Kinney / X-23 (Dafne Keen). Ao mesmo tempo em que
    se recusa a voltar à ativa, Logan é perseguido pelo mercenário
    Donald Pierce (Boyd Holbrook), interessado na menina.""",
    "http://br.web.img3.acsta.net/c_210_280/pictures/16/10/05/19/59/363613.jpg",  # noqa
    "https://www.youtube.com/watch?v=Div0iP65aZo",
    "2h 17min",
    "Ação, Ficção Científica"
    )

alfa = media.Movie(
    "Alfa",
    """Há 20.000 anos, em plena Era do Gelo, um jovem foi ferido durante uma
    caçada e seus companheiros partiram, pensando que ele estava morto.
    O jovem acorda e encontra um lobo que foi abandonado.
    O homem e o lobo tentam sobreviver juntos.""",
    "https://m.media-amazon.com/images/M/MV5BODI4OTk1ODY3N15BMl5BanBnXkFtZTgwMDI1MTcwNjM@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=uIxnTi4GmCo",
    "1h 37min",
    "Drama, Mistério"
)

oLoboDeWallStreet = media.Movie(
    "O Lobo de Wall Street",
    """Jordan Belfort é um ambicioso corretor da bolsa de valores que cria um
    verdadeiro império, enriquecendo de forma rápida, porém ilegal.
    Ele e seus amigos mergulham em um mundo de excessos, mas seus métodos
    ilícitos despertam a atenção da polícia.""",
    "https://upload.wikimedia.org/wikipedia/pt/8/8d/The_Wolf_of_Wall_Street.jpg",  # noqa
    "https://www.youtube.com/watch?v=PoSCUsNQVtw",
    "2h 59min",
    "Biografia"
)

naNaturezaSelvagem = media.Movie(
    "Na Natureza Selvagem",
    """Christopher McCandless, filho de pais ricos, se forma na universidade
    de Emory como um dos melhores estudantes e atletas. Porém, em vez de em
    embarcar em uma carreira prestigiosa e lucrativa, ele escolhe doar suas
    economias para caridade, livrar-se de seus pertences e
    viajar pelo Alasca.""",
    "https://upload.wikimedia.org/wikipedia/pt/8/8a/Into-the-wild.jpg",
    "https://www.youtube.com/watch?v=g7ArZ7VD-QQ",
    "2h 28min",
    "Drama, Aventura"
)

detonaRalph = media.Movie(
    "Detona Ralph",
    """Ralph está cansado de ser desprezado no seu próprio jogo de fliperama.
    Para ganhar a atenção do herói Felix e todos os outros personagens,
    o vilão tem um plano e sai em busca de uma medalha,
    com a intenção de provar o seu valor.""",
    "http://3.bp.blogspot.com/-fb1bk17945I/UUSOJHh-b1I/AAAAAAAAFFo/DKu2yKoJNTQ/s1600/Detona-Ralph-poster-brasil.jpg",  # noqa
    "https://www.youtube.com/watch?v=q7vk_FS55KQ",
    "1h 48min",
    "Animação"
)

# Objects to popular the site with data
movies = [
    extraordinario,
    belezaOculta,
    logan,
    alfa,
    oLoboDeWallStreet,
    naNaturezaSelvagem,
    detonaRalph
]
# creating static page through the movie list
freshTomatoes.open_movies_page(movies)
