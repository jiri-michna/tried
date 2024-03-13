from pprint import pprint

urolosy = ["https://image-comic.pstatic.net/webtoon/783862/19/20220209192204"\
           "_6f27e2fd3a037a7378b33a18594c6a1c_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/20/20220216161446"\
"_6cd1b7dc465b6c5e077c82808cef1fde_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/21/20220302124413"\
"_2a464c5326855291bd009bc7607327f8_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/22/20220302140534"\
"_883524071854f8178d8915a1a31b46ba_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/23/20220309154257"\
"_28e70b715c797ac8cbe2e63f189a55a0_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/24/20220316214031"\
"_4a662994556ebb8a28cbd6d8229f9009_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/25/20220323112225"\
"_2ad16feb86eeb4e3ebaa3027ac28bd73_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/26/20220330150612"\
"_98543be140a8d853de465eed1acd22db_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/27/20220406185351"\
"_2c0be40589eea7cfdeb4c9f6469854e6_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/28/20220413104010"\
"_387b72d9027d58aac2f49536f356a60c_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/29/20220420212002"\
"_608f1993a11d7b17d132c0542686adcf_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/30/20220427162507"\
"_323058138de88b9ea0906d72f20bdd60_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/31/20220504151053"\
"_cde6e3b2f0d96c8a8b2345bc8f38b244_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/32/20220511184849"\
"_ac7945c843e49dc525082e17d00493e8_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/33/20220518163251"\
"_b1df805001cbe476b2751176ad252a4f_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/34/20220525105014"\
"_50fbbf2c7f5450b0ca2b9ca86701ee3c_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/35/20220601163753"\
"_816fc5af1b71f2f724ed491c99806f86_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/36/20220608211344"\
"_94275d98715e83053780c438282a143c_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/37/20220615221108"\
"_adcb497e7c304d74bbcf81a1775679c7_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/38/20220622180140"\
"_50b1b6d0749d8c1278f5ad34290bfc81_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/39/20220727141000"\
"_0a9a37830a93e48273e9018831f84d27_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/40/20220706150744"\
"_e66a9930c268d576a4f5e36b8a8b4599_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/41/20220713202050"\
"_8b26ef137739c14fb0d8cd7c6ad35689_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/42/20220720214626"\
"_3bbea462b640d6d766d261759d4451f1_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/43/20220727202452"\
"_c099907482e7f3ea85a779d722be37e9_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/44/20220810140811"\
"_3a23a8e5e5d0003ae4cb1c84b2d38630_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/45/20220817154722"\
"_980abb2a77b89edb033c9a4252ecdb29_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/46/20220824210209"\
"_0a029a0121d4915251b311c7bb542b56_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/47/20220831193619"\
"_82686577b64ae021629641da37bc8944_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/48/20221012151117"\
"_875205ce54181e9bd86f897c70a16eef_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/49/20220914210317"\
"_49526417c2f27903b334c13e2c51d177_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/50/20220921232912"\
"_7477b3cf2ca18fe0d7b8cbca3bc2c1a1_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/51/20220928210710"\
"_e5b98f19d3b6c81b9dc89f950d8a7655_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/52/20221027185141"\
"_05c9e096978515359ffef72381662186_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/53/20221012202046"\
"_8720dd0dc3ed81b737850cfa916d3f69_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/54/20221019183418"\
"_7bb48d7a3bb4aa7533bf5157c72b5f53_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/55/20221027185215"\
"_9683b280b4749b2e4a88eec8936c98f4_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/56/20221102175021"\
"_4ad747e58a5aa01037ba0d836888ff42_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/57/20221123150112"\
"_35865674e3a134ab65e2f79f9d66b9d8_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/58/20221130190544"\
"_6bd571a08476e0460d4f380b7e3b1e4d_IMAG01_",
"https://image-comic.pstatic.net/webtoon/783862/59/20221214142758"\
"_0a58378a25f9ef376e0c5459581325cb_IMAG01_"]

def iwonder(n=0):
    n = n
    ch = 0
    res = " "
    while ch < 125:
        res += f"<img src= \"{urolosy[n]}{ch+1}.jpg\" alt=\"\" />\n"
        ch = ch+1
    writepath = 'templates/manga.html'
    mode = 'w+'
    with open(writepath, mode) as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang=\"en\">\n")
        f.write("<head>\n")
        f.write("   <meta charset=\"UTF-8\">\n")
        f.write("   <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
        f.write("   <title>Python to manga</title>\n")
        f.write(    
                "<link href=\"{{ url_for('static', filename='styles/style.css')}}\" \
                rel=\"stylesheet\" />\n"
                )
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<h1>MANGA HERE<h1/>")
        f.write("   " + res)
        f.write("   <h1>Input numero 0-idk</h1>\n")
        f.write("   <form action=\"/manga\">\n")
        f.write("       <input type=\"number\" name=\"n\" id=\"n\" \
                placeholder=\"Enter a numero\" />\n")
        f.write("       <button type=\"submit\">Clicke</button>\n")
        f.write("   </form>\n")
        f.write("</body>\n")
        f.write("</html>\n")
        f.close()
    return res



if __name__ == "__main__":
    print('\n*** Inmuputo numero')
    n = int(input("\nNumero here: "))
    res = iwonder(n)
    print("\n")
    pprint(res)
