#MUKHLIS SIRAJUDDIN
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency

sns.set(style='whitegrid')
days= pd.read_csv('day.csv')
# mencari data dengan penyewa paling banyak
cari = (days['cnt'] > 4548)
cari_data = days[cari]
musim = cari_data['season'].unique()
total1 = days[cari].shape[0]

musim_1 = (days['season'] == 1)
total_musim_1 = cari & musim_1
season1 = days[total_musim_1].shape[0]

musim_2 = (days['season'] == 2)
total_musim_2 = cari & musim_2
season2 = days[total_musim_2].shape[0]

musim_3 = (days['season'] == 3)
total_musim_3 = cari & musim_3
season3 = days[total_musim_3].shape[0]

musim_4 = (days['season'] == 4)
total_musim_4 = cari & musim_4
season4 = days[total_musim_4].shape[0]

# mencari jumlah data dengan penyewa paling sedikit
cari1 = (days['cnt'] < 4548)
cari_data1 = days[cari1]

musim1 = cari_data1['season'].unique()
total11 = days[cari1].shape[0]

musim_11 = (days['season'] == 1)
total_musim_11 = cari1 & musim_11
season11 = days[total_musim_11].shape[0]

musim_22 = (days['season'] == 2)
total_musim_22 = cari1 & musim_22
season22 = days[total_musim_22].shape[0]

musim_33 = (days['season'] == 3)
total_musim_33 = cari1 & musim_33
season33 = days[total_musim_33].shape[0]

musim_44 = (days['season'] == 4)
total_musim_44 = cari1 & musim_44
season44 = days[total_musim_44].shape[0]

terbesar = np.array([['musim 1', season1],['musim 2',season2], ['musim 3',season3], ['musim 4',season4]])
terkecil = np.array([['musim 1', season11],['musim 2',season22], ['musim 3',season33], ['musim 4',season44]])

### STREAMLIT
st.header("BIKE SHARING")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/00_2141_Bicycle-sharing_systems_-_Sweden.jpg/800px-00_2141_Bicycle-sharing_systems_-_Sweden.jpg")
st.write(
    """
    Hallo, terimakasih telah mengunjungi dashboard kami. Dashboard ini 
    berisi visualisasi penyewaan sepeda pada sebuah perusahaan dalam periode waktu tertentu.  
    """
)



st.subheader('Musim-musim dengan jumlah penyewaan paling banyak')


x = [0, 1, 2, 3]
y = [season1, season2, season3, season4]

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x, y, align ='center')

ax.set_title('Musim Dengan Jumlah Penyewaan Terbanyak')
ax.set_ylabel('Jumlah Hari')
ax.set_xlabel('Musim')

ax.set_xticks(x)
ax.set_xticklabels(('Musim 1', 'Musim 2', 'Musim 3', 'Musim 4'))

st.pyplot(fig)
st.write(
    """
    Pada grafik di atas terlihat bahwa musim ke-tiga merupakan musim denga jumlah penyewaan sepeda terbanyak dalam kurun waktu 2 tahun, dengan total hari sebanyak 143.
    diikuti musim ke-dua, musim ke-empat, dan terakhir musim ke-satu
    """
)
st.subheader('Musim-musim dengan jumlah penyewaan paling sedikit')

x1 = [0, 1, 2, 3]
y2 = [season11, season22, season33, season44]

fig1, ax = plt.subplots(figsize=(10,5))
ax.bar(x1, y2, align ='center')

ax.set_title('Musim Dengan Jumlah Penyewaan Paling Sedikit')
ax.set_ylabel('Jumlah Hari')
ax.set_xlabel('Musim')

ax.set_xticks(x)
ax.set_xticklabels(('Musim 1', 'Musim 2', 'Musim 3', 'Musim 4'))

st.pyplot(fig1)
st.write(
    """
    Pada grafik diatas terlihat bahwa musim pertama tercatat sebagai musim dengan jumlah penyewaan paling sedikit dengan total hari sebanyak 165. 
    Selama periode hari ini jumlah penyewaan sepeda dibawah 50 % dari jumlah penyewaan terbanyak yang pernah tercatat dalam periode 2011-2012. 
    """
)
st.subheader('5 Hari teratas dengan jumlah penyewa paling banyak')

data_terbanyak = days.nlargest(5, 'cnt')
tanggal = data_terbanyak[["dteday", "casual", "registered","cnt"]]
tanggal.head()
fig3, ax = plt.subplots(nrows=1, ncols=1)
sns.barplot(x="dteday", y="cnt", data=tanggal.head(), ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig3)
st.write(
    """
    Tabel di atas menunjukkan 5 hari teratas dengan jumlah penyewaan terbanyak.
    Terlihat bahwa pada tanggal 15-09-2012 total penyewaan sebesar 8.714 yang mana ini merupakan penyewaan terbanyak selama periode 2 tahun. Diikuti tanggal
    29/09, 22/09, 23/03, dan 19/05 yang terjadi pada tahun yang sama yaitu 2012, dengan total penyewaan berturut-turut yaitu 8.555, 8.395, 8.362 dan 8.294.
  """
)
st.subheader('Kesimpulan')
st.write(
    """
    1. Musim ke-tiga merupakan musim dimana jumlah penyewaan terbanyak dengan total hari dimana penyewaan diatas 50% dari total penyewaan terbanyak adalah 143 hari. Dan
    musim pertama merupakan musim dimana jumlah penyewaan paling sedikit dengan total hari dimana penyewaan dibawah 50% dari total penyewaan terbanyak adalah 165 hari.
    """)
st.write(
    """
    2. Tanggal 15-09-2012 merupakan hari dimana jumlah penyewaan terbanyak selama periode 2011-2012.
    """)





st.caption('Copyright (c) 2023 - Mukhlis Sirajuddin')