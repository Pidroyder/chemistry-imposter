# Импорт библиотек
from random import randint


def start(button, label, members_count: int, on_finish=None):
    if not members_count:
        label.text = 'Введите корректное количиство игроков'
        return

    elements = ['H\nводород', 'He\nгелий', 'Li\nлитий', 'Be\nбериллий', 'B\nбор', 'C\nуглерод', 'N\nазот',
                'O\nкислород', 'F\nфтор', 'Ne\nнеон', 'Na\nнатрий', 'Mg\nмагний', 'Al\nалюминий', 'Si\nкремний',
                'P\nфосфор', 'S\nсера', 'Cl\nхлор', 'Ar\nаргон', 'K\nкалий', 'Ca\nкальций', 'Sc\nскандий', 'Ti\nтитан',
                'V\nванадий', 'Cr\nхром', 'Mn\nмарганец', 'Fe\nжелезо', 'Co\nкобальт', 'Ni\nникель', 'Cu\nмедь',
                'Zn\nцинк', 'Ga\nгаллий', 'Ge\nгерманий', 'As\nмышьяк', 'Se\nселен', 'Br\nбром', 'Kr\nкриптон',
                'Rb\nрубидий', 'Sr\nстронций', 'Y\nиттрий', 'Zr\nцирконий', 'Nb\nниобий', 'Mo\nмолибден',
                'Tc\nтехнеций', 'Ru\nрутений', 'Rh\nродий', 'Pd\nпалладий', 'Ag\nсеребро', 'Cd\nкадмий', 'In\nиндий',
                'Sn\nолово', 'Sb\nсурьма', 'Te\nтеллур', 'I\nиод', 'Xe\nксенон', 'Cs\nцезий', 'Ba\nбарий', 'La\nлантан',
                'Ce\nцерий', 'Pr\nпразеодим', 'Nd\nнеодим', 'Pm\nпрометий', 'Sm\nсамарий', 'Eu\nевропий',
                'Gd\nгадолиний', 'Tb\nтербий', 'Dy\nдиспрозий', 'Ho\nгольмий', 'Er\nэрбий', 'Tm\nтулий', 'Yb\nиттербий',
                'Lu\nлютеций', 'Hf\nгафний', 'Ta\nтантал', 'W\nвольфрам', 'Re\nрений', 'Os\nосмий', 'Ir\nиридий',
                'Pt\nплатина', 'Au\nзолото', 'Hg\nртуть', 'Tl\nталлий', 'Pb\nсвинец', 'Bi\nвисмут', 'Po\nполоний',
                'At\nастат', 'Rn\nрадон', 'Fr\nфранций', 'Ra\nрадий', 'Ac\nактиний', 'Th\nторий', 'Pa\nпротактиний',
                'U\nуран', 'Np\nнептуний', 'Pu\nплутоний', 'Am\nамериций', 'Cm\nкюрий', 'Bk\nберклий', 'Cf\nкалифорний',
                'Es\nэйнштейний', 'Fm\nфермий', 'Md\nменделевий', 'No\nнобелий', 'Lr\nлоуренсий', 'Rf\nрезерфордий',
                'Db\nдубний', 'Sg\nсиборгий', 'Bh\nборий', 'Hs\nхассий', 'Mt\nмейтнерий', 'Ds\nдармштадтий',
                'Rg\nрентгений', 'Cn\nкоперниций', 'Nh\nнихоний', 'Fl\nфлеровий', 'Mc\nмосковий', 'Lv\nливерморий',
                'Ts\nтеннессин', 'Og\nоганесон']
    element = elements[randint(0, members_count - 1)]
    members = [False for i in range(members_count)]

    members[randint(0, members_count - 1)] = True

    state = {'index': 0, 'showing_role': False}

    label.text = 'Передайте телефон человеку и нажмите еще раз'

    def on_click(instance):
        show_roles(button, label, members_count,
                   element, members, state, on_finish)

    button.bind(on_press=on_click)
    button._role_handler = on_click


def show_roles(button, label, members_count: int, element: str,
               members: list, state: dict, on_finish=None):
    i = state['index']

    if not state['showing_role']:
        if members[i]:
            label.text = 'Ты шпион. Нажми и передай телефон следующему.'
            label.color = (1, 0, 0, 1)
        else:
            label.text = f'{element}\nНажми и передай телефон следующему.'
            label.color = (0, 1, 0, 1)
        state['showing_role'] = True
        return

    state['index'] += 1
    state['showing_role'] = False

    if state['index'] >= members_count:
        label.text = 'Да начнется супный день'
        label.color = (1, 0, 1, 1)
        old = getattr(button, '_role_handler', None)
        if old is not None:
            button.unbind(on_press=old)

        def reset(instance):
            button.unbind(on_press=reset)
            label.text = 'Нажмите чтобы начать игру'
            label.color = (0, 0, 1, 1)
            if on_finish is not None:
                on_finish()

        button.bind(on_press=reset)
        button._role_handler = reset
        return

    label.text = 'Передайте телефон человеку и нажмите ещё раз'
    label.color = (0, 0, 1, 1)
