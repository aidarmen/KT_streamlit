import streamlit as st
import pandas as pd
import numpy as np
import datetime

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Using the "with" syntax
with st.form(key='my_form'):

    df = pd.read_csv('map.csv')

    q = {
        0: 'Плановая дата исследования',
        1: 'Фактическая дата исследования',
        2: 'ФИО исполнителя',
        3: 'РДТ',
        4: 'Название Области/Район/Города',
        5: 'Название населенного пункта',
        6: 'Тип населенного пункта (город/ село)',
        7: 'Тип улицы (проспект/ бульвар/улица/переулок)',
        8: 'Наименование улицы',
        9: 'Адрес первого (здания/сооружения/дома) расположенного на улице',
        10: 'Номер дома к адресу первого расположенного на улице',
        11: 'Адрес последнего (здания/сооружения/дома) расположенного на улице',
        12: 'Номер дома к адресу последнего расположенного на улице',
        13: 'Протяженность улицы (в метрах)',
        14: 'Координаты начала улицы (Широта, Долгота)',
        15: 'Координаты конца улицы (Широта, Долгота)',
        151: 'Наименование пересекающихся улиц',
        16: 'Количество домов пересекающихся с другими улицами',
        17: 'Количество жилых домов',
        18: 'Количество многоквартирных домов',
        19: 'Номера многоквартирных домов',
        20: 'Количество частных домов',
        21: 'Количество нежилых домов',
        22: 'Количество домов на четной стороне',
        23: 'Номера домов на четной стороне',
        24: 'Количество домов на нечетной стороне',
        25: 'Номера домов на нечетной стороне',
        26: 'Количество нежилых зданий',
        27: 'Номера нежилых зданий',
        28: 'Количество остановок,маршрутов городского транспорта на данной улице',
        29: 'Номера маршрутов общественного транспорта',
        30: 'Уровень благоустройства улицы',
        31: 'Количество билбордов и других рекламных конструкций, установленные на улице',
        32: 'Размеры билбордов и других ул. рекламных конструкций',
        33: 'Количество опор связи на улице',
        34: 'Адреса домов, рядом с которыми установлена первая и последняя опора связи',
        35: 'Количество распределительных шкафов/коробок связи',
        36: 'Адреса домов, рядом с которыми установлен первый и последний распределительный шкаф/коробка связи',
        37: 'Присутствие АО"Казахтелеком"',
        38: 'Технологии ШПД',
        39: 'Конкуренты',
        40: 'Технологии ШПД Конкурентов',
        41:"Мобильная связь (Уровень сигнала)",
        42: 'Мобильный ШПД',
        43: 'Наличие спутниковых антенн',
        44: "Перечень организаций (школы, торговые центры и т.д.)",
        45: "Уровень благосостояние жильцов проживающих по данной улице"


    }

    st.header('Анкета')

    st.date_input(
    q[0],
    datetime.date.today(),
    key='a0')

    st.date_input(
    q[1],
    datetime.date.today(),
    key='a1')

    st.text_input(
    q[2],
    "",
    key='a2')


    st.session_state.options_rdt = [
        '',
        'Восточная региональная дирекция телекоммуникаций',
        'Западная региональная дирекция телекоммуникаций',
        'РДТ "Алматытелеком"',
        'Северная региональная дирекция телекоммуникаций',
        'Центральная региональная дирекция телекоммуникаций',
        'Южная региональная дирекция телекоммуникаций'
    ]

    st.selectbox(
        q[3],
        st.session_state.options_rdt,
        key='a3')

    st.session_state.options_region = np.unique(df.loc[df['rdt'] == st.session_state.a3, 'region'].to_numpy())


    st.selectbox(
    q[4],
    st.session_state.options_region,
    key='a4')


    st.session_state.options_town = np.unique(df.loc[(df['rdt'] == st.session_state.a3 ) & (df['region'] == st.session_state.a4 ), 'isb_town'].to_numpy())

    st.selectbox(
         q[5],
         st.session_state.options_town,
    key='a5'
    )

    st.session_state.options_gts_sts = [
        'ГТС',
        'СТС'
    ]

    st.selectbox(
         q[6],
         st.session_state.options_gts_sts,
         key='a6'
    )


    st.session_state.option_street_type = [
    'Ал.',
    'Блв.',
    'ЖК',
    'ЖМ',
    'ЖР',
    'Кв.',
    'Мкр.',
    'Наб.',
    'Пер.',
    'Пл.',
    'Прз.',
    'Про.',
    'Прс.',
    'Рзд.',
    'Тр.',
    'Ул.'
    ]

    st.selectbox(
     q[7],
     st.session_state.option_street_type,
     key='a7')

    st.session_state.options_street = np.unique(df.loc[(df['rdt'] == st.session_state.a3) &
                                                       (df['region'] == st.session_state.a4) &
                                                       (df['isb_town'] == st.session_state.a5),
                                                       'isb_street'].to_numpy())

    st.selectbox(
     q[8],
     st.session_state.options_street,
    key='a8')

    st.selectbox(
     q[9],
     st.session_state.options_street,
    key='a9')

    st.text_input(
     q[10],
     "",
    key='a10')

    st.selectbox(
     q[11],
     st.session_state.options_street,
    key='a11')

    st.text_input(
     q[12],
     "",
    key='a12')

    st.number_input(
     q[13],
    step=1,
    key='a13')

    st.text_input(
     q[14],
     "",
    key='a14')

    st.text_input(
     q[15],
     "",
    key='a15')


    st.multiselect(label=q[151],
    options= st.session_state.options_street,
    key = 'a151')



    st.number_input(
     q[16],
    step=1,
    key='a16')


    st.number_input(
     q[17],
    step=1,
    key='a17')


    st.number_input(
     q[18],
    step=1,
    key='a18')

    st.text_input(
     q[19],
     "",
    key='a19')

    st.number_input(
     q[20],
    step=1,
    key='a20')

    st.number_input(
     q[21],
    step=1,
    key='a21')

    st.number_input(
     q[22],
    step=1,
    key='a22')

    st.text_input(
     q[23],
     "",
    key='a23')

    st.number_input(
     q[24],
    step=1,
    key='a24')

    st.text_input(
     q[25],
     "",
    key='a25')

    st.number_input(
     q[26],
    step=1,
    key='a26')

    st.text_input(
     q[27],
     "",
    key='a27')


    st.number_input(
     q[28],
    step=1,
    key='a28')

    st.text_input(
     q[29],
     "",
    key='a29')

    st.text_input(
     q[30],
     "",
    key='a30')

    st.number_input(
     q[31],
    step=1,
    key='a31')

    st.text_input(
     q[32],
     "",
    key='a32')

    # 33: 'Количество опор связи на улице',
    st.number_input(
     q[33],
    step=1,
    key='a33')


    # 34: 'Адреса домов, рядом с которыми установлена первая и последняя опора связи',
    st.text_input(
     q[34],
     "",
    key='a34')

    # 35: 'Количество распределительных шкафов/коробок связи',
    st.number_input(
     q[35],
    step=1,
    key='a35')

    # 36: 'Адреса домов, рядом с которыми установлен первый и последний распределительный шкаф/коробка связи',
    st.text_input(
     q[36],
     "",
    key='a36')

    # 37: 'Присутствие АО"Казахтелеком"',


    st.session_state.yes_no = [
    'да',
    'нет'
    ]

    st.selectbox(
     q[37],
     st.session_state.yes_no,
     key='a37')


    # 38: 'Технологии ШПД',

    st.session_state.internet_tech = [
    'нету',
    'DSL',
    'FTTh',
    'FTTb',
    'WiMax'
    ]

    st.multiselect(q[38],
    options =st.session_state.internet_tech,
    key='a38')

    # 39: 'Конкуренты',

    st.session_state.oppositions = [
    'нету',
    'Beeline',
    'AlmaTV',
    'TransTelecom'

    ]

    st.multiselect(q[39],
    options =st.session_state.oppositions,
    key='a39')

    # 40: 'Технологии ШПД Конкурентов',
    st.multiselect(q[40],
    options =st.session_state.internet_tech,
    key='40')

    # 41: "Мобильная связь (Уровень сигнала)",

    st.session_state.mob_signal = [
    'удовлетворительно',
    'не удовлетворительно'
    ]

    st.selectbox(q[41],
    st.session_state.mob_signal,
    key='41')

    # 42: 'Мобильный ШПД',
    st.session_state.mob_network = [
    'нету',
    '2G',
    '3G',
    '4G'
    ]

    st.selectbox(q[42],
    st.session_state.mob_network,
    key='42')

    # 43: 'Наличие спутниковых антенн',
    st.selectbox(q[42],
    st.session_state.yes_no,
    key='42')

    # 44: "Перечень организаций (школы, торговые центры и т.д.)",

    st.text_input(
     q[44],
     "",
    key='a44')

    # 45: "Уровень благосостояние жильцов проживающих по данной улице"

    st.text_input(
     q[45],
     "",
    key='a45')
    submit_button = st.form_submit_button(label='отправить')