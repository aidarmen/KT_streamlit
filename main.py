import streamlit as st
import pandas as pd
import numpy as np
import datetime
import gspread

cred = {
    "type": "service_account",
    "project_id": "focused-elysium-340604",
    "private_key_id": "b4d9ed4edcf1403742b7783bff2a3cbf2ea4e6f8",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDIcsuFOPcIGXUO\nGgvuI7jEY0c2DHIA29pjNSY9MWPo0NlfYwOnOImpRdpEV+5LsdGTbCThfG+TZxfW\nmxJyt+HSbjycl6SIDmbKzZN8bgwU4KyxrsBU2hfiB5PjYKgOwKaAt+/QuW3ZC2aG\n9DeMS906O0zO5k3acxMgKWPjv3PMFjyen4AFON+f256PE07aqJpLYmRU1g4kLAlX\nmLwpYEygik8EJfKwBevwtxJjVu8fiaJjAo8X6UMmLieH2EZ5K0tPsji7MhKZwvy9\ninbewE5MerrI2AsIyZr0UAfeaom04UAynHtRGt+5IKxGQilHqhzJjiVpfk4hNi7E\nWExCb90vAgMBAAECggEAUQYuBDTpjgmUSlX2+pTP6/phX5SaRISZ+z4RreyYARTi\nuO7yHBb7dkP5HWUZutku6NNu+QJuq3uhpCrcwyhXDNNohre5VxHTNSjx8/sbwRis\nVcpYjjP2MXR0sBVy+TugUimHs6wwnepA0E5JYdmMnCw6OOvZDnMziO2SJg5OhXDE\nfFBNp1jA5uYri5J1KkaYnLBns8BGi26GHdVpEa5J+MGb24h04nuU5HfafpMP+Vty\nhXp43tnpsdOf75QNkFg5JR3QNzYsd3J6OkQj6MtLCbiWVUMtcZWYLt/sT9kusAz2\nj96VTrRKZx6p5+JEmPuVqKaWRvTYpN0aJ3YXTilQ+QKBgQDlTjbwDS/obF3VXX4e\nR5fdr1RNQUU0MdPM8tuatwrkKakcgfLZq/9le5f1mwOWKSQokUvZFb0OjAKOqZ43\n5wp1tM/UP6mF59SjJeW1lyf4aSoX4EypVDZassxGw+z+nPryo55s14br0zp+OFkt\n2azC/7S68eEri8tCVscElkcmVQKBgQDfyJP9veT+vf1/HVPlGpdBh8zCkPO3pzWE\nzMNTdIYY0OkOvfTl+4bQ+7DA+T9PN6ubMENVSp0SXcxfrTQBj0ePxapvzGeg7Lwm\ngMkUOTatGjLSzYyGWi5Tc/ynkIvq7PUrXsJ6dqnUiRa15pi9eTeRbfb/PmJps4qw\nFSl3LTYRcwKBgQDMSBbXWtgwVsJtgAIIVb2syDLxNFHDwxQuhLkxpxoz1A2NkRNZ\n6kn4Ddh9/OCAGRzWa0LIHf60g/UPRXrn0JPX8wIn06Nh4PvlcLCpSwVX39CZPsDt\nJVHbEWi9LnTnC9Dg8vUDgCr50s9MfUStfTvU6NsIpM317m9hJU/d/UdblQKBgQCt\n46FDoYRIgn9xf+uJ8iColgqBAbuv8KlAmRAKUFhG/kaq4uZisxFuYLVXLhaIytx5\nCYa4xvLIq8Q8cE0iDSDxUgp/NxkrTeliDd6x7UdUOTBW58wTNg4bYNxppINkuF5G\nJir+mCidcy0HibkUOhX41rcAXYyBUDcrXjZLWgFSiwKBgQCT79Q4GIN0MqJEvQxs\nvUfMF96gsJ9cEGGjROtw/qlpaPJBhpmNSuHc6gKAxLDneIdt5nBxyo+lZOpzMIve\ntwnocYa/D8RCOYBX1S3pecI72ss82N+Ek/o2+PNt3nbZ+wxBhNlOIMiH3LxKOsLM\nuzNty1dOJ97/L0ED5IZ9sESCwg==\n-----END PRIVATE KEY-----\n",
    "client_email": "temp-606@focused-elysium-340604.iam.gserviceaccount.com",
    "client_id": "113559229310896807100",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/temp-606%40focused-elysium-340604.iam.gserviceaccount.com"
}

@st.cache
def long_running_function():
    sa = gspread.service_account_from_dict(cred)
    sh = sa.open("KT_DATA_ANKETA")
    st.session_state.sh = sa.open("KT_DATA_ANKETA")
    wks = sh.worksheet('map')

    st.session_state.df = pd.DataFrame(wks.get_all_records()).astype('str')

    # return pd.DataFrame(wks.get_all_records())
# df = pd.read_csv('map.csv')
df = pd.read_csv('map.csv')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)





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
    45: "Уровень благосостояние жильцов проживающих по данной улице",
    46: 'Наименование пересекающихся улиц'

}

st.header('Анкета')

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Пароль", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Пароль", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 пароль не правильный")
        return False
    else:
        # Password correct.
        return True

if check_password():

    # long_running_function()
    st.session_state.df = df

    st.date_input(
    q[0],
    datetime.date.today(),
    key='a0')

    st.date_input(
    q[1],
    datetime.date.today(),
    key='a1',
    disabled = True)

    st.text_input(
    q[2],
    "",
    key='a2')


    options_rdt = [
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
        options_rdt,
        key='a3')

    st.session_state.options_region = np.unique(
        st.session_state.df.loc[st.session_state.df['rdt'] == st.session_state.a3, 'region'].to_numpy())


    st.selectbox(
    q[4],
    st.session_state.options_region,
    key='a4')


    st.session_state.options_town = np.unique(
        st.session_state.df.loc[(st.session_state.df['rdt'] == st.session_state.a3 ) &
                                (st.session_state.df['region'] == st.session_state.a4 ), 'isb_town'].to_numpy())

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

    st.session_state.options_street = np.unique(st.session_state.df.loc[(st.session_state.df['rdt'] == st.session_state.a3) &
                                                       (st.session_state.df['region'] == st.session_state.a4) &
                                                       (st.session_state.df['isb_town'] == st.session_state.a5),
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


    st.multiselect(label=q[46],
    options= st.session_state.options_street,
    key = 'a46')



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
    '',
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
    '',
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
    key='a40')

    # 41: "Мобильная связь (Уровень сигнала)",

    st.session_state.mob_signal = [
    'удовлетворительно',
    'не удовлетворительно'
    ]

    st.selectbox(q[41],
    st.session_state.mob_signal,
    key='a41')

    # 42: 'Мобильный ШПД',
    st.session_state.mob_network = [
    '',
    '2G',
    '3G',
    '4G'
    ]

    st.selectbox(q[42],
    st.session_state.mob_network,
    key='a42')

    # 43: 'Наличие спутниковых антенн',
    st.selectbox(q[43],
    st.session_state.yes_no,
    key='a43')

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






    if st.button(label='отправить') :

        st.session_state.all_input_filled = True
        for i in range(len(q)):
            key = 'a' + str(i)
            if not isinstance(st.session_state[key],int) and not isinstance(st.session_state[key], datetime.date):
                if len(st.session_state[key]) == 0:
                    st.session_state.all_input_filled = False

        if st.session_state.all_input_filled:
            st.session_state.wks = st.session_state.sh.worksheet('result')
            st.session_state.values_list = list()
            for i in range(len(q)):
                key ='a'+str(i)
                if isinstance(st.session_state[key], datetime.date):
                    st.session_state.values_list.append(st.session_state[key].strftime("%d/%m/%Y"))
                elif isinstance(st.session_state[key],list):
                    st.session_state.values_list.append(', '.join(map(str, st.session_state[key])))
                else:
                    st.session_state.values_list.append(st.session_state[key])

            st.session_state.wks.append_row( st.session_state.values_list)
            for key in st.session_state.keys():
                del st.session_state[key]

            st.success('отправлено')
            st.experimental_rerun()
        else:

            st.warning('поле не заполнено')
