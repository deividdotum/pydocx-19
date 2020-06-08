schemas = {
    "nome_paciente": r'nome do paciente:\s(.+)cpf:',
    "cpf": r'cpf:(\d+)',
    "idade": r'idade:\s(\d{2})',
    "data_nascimento": r'data de nascimento:(\s\d{2}\/\d{2}\/\d{2,4})',
    "sexo": r'sexo\s\[\s+(\d)\s+]',
    "gestante": r'gestante\s\[\s+(\d)\s+]',
    "raca_cor": r'raca\/cor\s\[\s+(\d)\s+]',
    "etinia": r'etnia(.+)',
    "escolaridade": r'escolaridade\s\[\s+(\d)\s+]',
    "ocupacao": r'ocupacao\s?:\s?(.+)cns:',
    "nome_da_mae": r'nome\sda\smae:\s?(.+)+\n',
    "endereco": {
        "municipio": r'municipio:\s?(.+)estado:',
        "estado": r'estado:\s?(.+)bairro:',
        'bairro': r'bairro:\s+?(.+)zona',
        'zona': r'zona\s\[\s+(\d)\s+\]',
        'complemento': r'complemento:\s+(.+)\s',
    },
    'telefone': r'telefone:\s+(.+)complemento:',
    'trabalhap_ou_tem_contato_com_aves_ou_suinos': r'paciente\strabalha\sou\stem\scontato\scom\saves\sou\ssuinos\s\[\s+(\d)\s+\]',
    'data_inicio_sintomas': r'data inicio dos sintomas:\s+(\d{2}\/\d{2}\/\d{2,4})',
    'monitoramento_diario_ate_14_dias': r'monitoramento diario ate 14 dias:\s+(\d{2}\/\d{2}\/\d{2,4})',
    "sintomas": {
        'dor_de_garganta': r'\[(.+)\]\sdor\sde\sgarganta',
        'dispineia': r'\[(.+)\]\sdispneia',
        'febre': r'\[(.+)\]\s+?febre',
        'tosse_seca': r'tosse\s+\[(.+)\]\s+?seca',
        'tosse_produtiva': r'seca\s+\[(.+)\]\s+?produtiva',
        'perda_de_olfato_e_paladar': r'\[(.+)\]\s+?perda\sde\solfato\se\spaladar',
        'dor_de_cabeca': r'\[(.+)\]\s+?dor\sde\scabeca',
        'dor_no_corpo': r'cabeca\s+\[(.+)\]\s+?dor\sno\scorpo',
        'outros_sintomas': r'outros\ssintomas:\s+(.+)?',
    },
    "frequencia_respiratoria": {
        "leve": r'\[(.+)\]leve\s?-\s+abaixo\s+?de\s+?20\s+?irm',
        "moderado": r'\[(.+)\]moderado',
        "grave": r'\[(.+)\]grave'
    },
    "fatores_de_risco": {
        "puerpera": r'\[(.+)\]puerpera',
        "sindrome_de_down": r'\[(.+)\]sindrome\sde\sdown',
        "doenca_hepatica_cronica": r'\[(.+)\]doenca\shepatica\scronica',
        "obesidade_imc": r'\[.+\]obesidade\s+imc(.+)',
        "diabetes_mellitus": r'\[(.+)\]diabetes\smellitus',
        "doenca_neurologica_cronica": r'\[(.+)\]doenca\sneurologica\scronica',
        "outros": r'outros\s(.+)',
        "imunodeficiencia_imunodepressao": r'\[(.+)\]imunodeficiencia\/imunodepressao',
        "doenca_renal_cronica": r'\[(.+)\]doenca\srenal\scronica',

    },
    "vacina_gripe": {
        "recebeu_vacina": r'recebeu vacina contra gripe.+\n+?\s+?.+?\s+?\n+?.+?\s+?\[(.+)\]',
        "dosesNum": r'recebeu vacina contra gripe.+\n+?\s+?.+?\s+?\n+?.+?\s+?.+\s+?\n+?(\d)',
        "data_ultima_dose": r'recebeu vacina contra gripe.+\n+?\s+?.+?\s+?\n+?.+?\s+?.+\s+?\n+?\d?\s+?\n+?(\d{2}\/\d{2}\/\d{2,4})'
    },
    "antiviral": {
        "tipo": r'data\sdo\sinicio\sdo\stratamento\s+?\[(.+)\]',
        "data_inicio_tratamento": r'data\sdo\sinicio\sdo\stratamento\s+?\[.+?\].+\n+(\d{2}\/\d{2}\/\d{2,4})'
    },
    "investigacao_diagnostica": {
        "RT-PCR_SARS-CoV-2": {
            "data": r'rt-pcr\sp\/\s+sars-cov-2\sdata:\s(\d{2}\/\d{2}\/\d{2,4})',
            "por": r'rt-pcr\sp\/\s+sars-cov-2\sdata:\s\d{2}\/\d{2}\/\d{2,4}\s+por\s+(.+)\('
        },
        "teste_rapido_Igm_Igg": {
            "data": r'teste\srapido\sigm\/igg\s+\s\sdata:\s(\d{2}\/\d{2}\/\d{2,4})',
            "por": r'teste\srapido\sigm\/igg\s+\sdata:\s\d{2}\/\d{2}\/\d{2,4}\s+por\s+(.+)\('
        },
        "outras": {
            "descricao": r'outro(.+)data:',
            "data": r'outro.+data:\s\d{2}\/\d{2}\/\d{2,4}',
            "por": r'outro.+data:\s\d{2}\/\d{2}\/\d{2,4}\s+por\s(.+)'
        },
    },
    "data_conclusao": r'conclusao\s+(\d{2}\/\d{2}\/\d{2,4})',
    "diagnostico": r'diagnostico\s+(\w+)',
    "cura": r'evolucao\s+\((.+)\)cura',
    "obito": r'evolucao\s+\(.+\)cura\s+\((.+)\)obito',
    "responsavel": r'resp\.\spela\snotificacao:\s(.+)',

    'acompanhamento': {
        "regex": r'\do\s+\n.?(?P<data>\d{2}\/\d{2}\/\d{2,4})\n+?.?(?P<hora>\d{2}:\d{2}:\d{2})\n+?(?P<descricao>.+)\n+(?P<responsavel>.+)',
        "list": True
    }
}
