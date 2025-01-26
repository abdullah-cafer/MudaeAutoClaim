# 💖✨ Mudae Otomatik Karakter Alma Botu ✨💖

[![Discord TOS İhlali - **AŞIRI DİKKATLE KULLANIN**](https://img.shields.io/badge/Discord%20TOS-İHLALİ-red)](https://discord.com/terms) ⚠️ **HESAP BANLANMA RİSKİ!** ⚠️

**🛑🛑🛑  DUR! DEVAM ETMEDEN ÖNCE BU ** **KRİTİK UYARIYI** **OKUYUN!** 🛑🛑🛑

Bu bot bir **KİŞİSEL BOT'tur (SELF-BOT)**. Kişisel botların kullanımı Discord tarafından **KESİNLİKLE YASAKTIR** ve **Hizmet Şartlarını İHLAL EDER**.

**🔥  BU BOTU KULLANIRSANIZ DİSCORD HESABINIZIN KALICI OLARAK ASKIYA ALINMASI VEYA BANLANMASI RİSKİNİ GÖZE ALIRSINIZ. 🔥**

**😱  DİSCORD TARAFINDAN SİZE KARŞI ALINAN HİÇBİR HESAP İŞLEMİNDEN SORUMLU DEĞİLİZ.  😱**

**⚠️  BU BOTU KENDİ RİSKİNİZLE KULLANIN! AŞIRI DİKKATLİ OLUN VE YALNIZCA TEHLİKELERİ TAM OLARAK ANLIYORSANIZ DEVAM EDİN.  ⚠️**

---

## 🚀 Mudae'de Otomasyonun Gücünü Serbest Bırakın! (Sorumlu Bir Şekilde!) 🚀

**Mudae Otomatik Karakter Alma Botu**, popüler Mudae Discord botunda işlemleri otomatikleştirmek için Python ile geliştirilmiş yardımcınız! Karakter koleksiyonunuzu kolaylaştırın, kakera kazancınızı en üst düzeye çıkarın ve Mudae oyununuzu bir sonraki seviyeye taşıyın! 🌟

**✨  Bu Botu Parlatan Temel Özellikler: ✨**

*   **👯‍♀️ Çoklu Hesap Ustalığı:**  **Aynı anda birden fazla Discord hesabını** çalıştırın! Tüm Mudae çabalarınızı tek bir komut dosyasından yönetin! 🚀
*   **🤖 Tam Otomatik Çekme ve Alma:**  Arkanıza yaslanın ve rahatlayın! Bot **otomatik olarak karakter çeker, alınabilir karakterleri ve kakerayı tespit eder ve sizin için alır!** ✨
*   **💎 Kakera Zekasıyla Alma:**  **Minimum `kakera` değerinizi** ayarlayın! Bot, **yüksek kakera değerine sahip karakterleri** almayı akıllıca önceliklendirir (veya isterseniz her şeyi alın!). 🧠
*   **🥇 Akıllı Alma Mantığı - Kazançlarınızı En Üst Düzeye Çıkarın!**  Sadece almak değil, **akıllıca almak!** Bot, yüksek değerli karakterlere öncelik verir ve hatta fırsat doğduğunda **ikinci alımlar** için `$rt` kullanır! 🏆
*   **🔄 Çekim Yenilemesi mi? Sorun Değil!**  Çekimleriniz mi bitti? Bot, **çekim tükenmesini otomatik olarak algılar ve sabırla** bir sonraki yenilemeyi bekler! ⏳
*   **✅ Alma Hakları? Her Zaman Kontrol Altında!**  Boşa harcanan komut yok! Bot, harekete geçmeden önce **alma kullanılabilirliğini doğrular**, verimliliği optimize eder. ⚡
*   **⏱️ Özelleştirilebilir Gecikmeler - İnsan Gibi Olun!**  **İnsan davranışını taklit etmek** ve **hız sınırlama riskini en aza indirmek** için gecikmeleri ayarlayın. 🤫
*   **🔑 Anahtar Modu - Kakera Toplama Steroidlerde!**  "Anahtar Modu"nu etkinleştirin ve bot, alma hakları kapalı olsa bile **acımasızca kakera çekmeye devam edecektir!** Toplamayı asla bırakmayın! 💰
*   **🗂️ Ön Ayar Gücü - Yapılandırma Kolaylaştı!**  **Tüm hesaplarınızın ayarlarını tek bir düzenli `presets.json` dosyasında yönetin!** Zirvedeki sadelik! 📂
*   **📊 Gerçek Zamanlı Konsol İzleme - Bilgilenin!**  Botu çalışırken izleyin! **Gerçek zamanlı günlükler ve durum güncellemeleri** doğrudan konsolunuzda! 👀
*   **📜 Ayrıntılı Günlük Kaydı - Hazinelerinizin İzini Sürün!**  **Tüm bot işlemlerinin ve alınan karakterlerin kaydını tutun!** Mudae geçmişiniz parmaklarınızın ucunda! 📖

---

## 🛠️ Dakikalar İçinde Başlayın! Kurulum Çok Kolay! 💨

1.  **🐍 Python Güç Merkezi:**  **Python 3.8 veya ÜZERİ** sürümünün yüklü olduğundan emin olun. [python.org](https://www.python.org/downloads/)'dan edinin! 🚀

2.  **📦 Temel Gereksinimleri Yükleyin:** Terminalinizi veya komut isteminizi açın ve gerekli Python kütüphanelerini pip kullanarak çalıştırın:

    ```bash
    pip install discord.py-self inquirer
    ```

3.  **📝 `presets.json` Yapılandırmanızı Oluşturun:**  `mudae_bot.py` ile aynı dizinde `presets.json` adında bir dosya oluşturun. Sihrin gerçekleştiği yer burası! ✨

    ```json
    {
      "BenimHarikaBotum1": {  // 🌟 Ön ayarınıza havalı bir isim verin!
        "token": "SİZİN_DİSCORD_HESAP_TOKENİNİZ_1",   // 🔑  Gizli hesap tokeniniz! (Kullanım bölümüne bakın!)
        "prefix": "!",                             // ⚙️  Bot komut ön eki (bunu muhtemelen çok kullanmayacaksınız)
        "channel_id": 123456789012345678,         // 💬  Discord Kanal Kimliği - botun çalıştığı yer! (Discord'dan alın!)
        "roll_command": "wa",                       // 🎲  Tercih ettiğiniz Mudae çekme komutu (wa, wg, ha, hg, w, h)
        "delay_seconds": 1,                         // ⏳  İşlemler arası gecikme (saniye, güvenlik için 0.8'in üzerinde tutun!)
        "mudae_prefix": "$",                        // 💰  Mudae'nin komut ön eki (genellikle $)
        "min_kakera": 50,                           // 💎  Karakter almak için minimum kakera değeri (her şeyi almak için 0)
        "key_mode": false                           // 🔑  Anahtar Modunu etkinleştirin mi? (doğru/yanlış - Kakera odaklı çekim için)
      },
      "KakeraAvcısıBotu": {   // 🚀 Başka bir harika ön ayar!
        "token": "SİZİN_DİSCORD_HESAP_TOKENİNİZ_2",
        "prefix": "?",
        "channel_id": 987654321098765432,
        "roll_command": "wg",
        "delay_seconds": 1.5,
        "mudae_prefix": "$",
        "min_kakera": 75,
        "key_mode": true
      }
      // ... Tüm hesaplarınız için daha fazla ön ayar ekleyin! 🚀🚀🚀
    }
    ```

    **🔍  `presets.json` Ayarları - Ayrıntılı Açıklama:**

    *   **`preset_name`**:  Ön ayarınız için **açıklayıcı bir ad** (örneğin, "AnaHesap", "AlternatifBot"). Bu, botları konsolda tanımlamanıza yardımcı olur.
    *   **`token`**: **SİZİN DİSCORD HESAP TOKENİNİZ!** Bu **SÜPER GİZLİDİR!** Nasıl alınacağını öğrenmek için "Kullanım" bölümüne bakın. **TOKENİNİZİ ASLA PAYLAŞMAYIN!** 🔒
    *   **`prefix`**:  Botun komut ön eki. Bunu muhtemelen çok kullanmayacaksınız, herhangi bir şey ayarlayın (örneğin, `!`, `?`, `.`).
    *   **`channel_id`**:  Botun çalışacağı **Discord Kanal Kimliği**. **Discord ayarlarında Geliştirici Modunu etkinleştirin** (Ayarlar -> Görünüm -> Gelişmiş), ardından **kanala sağ tıklayın ve "Kimliği Kopyala"yı seçin**. 💬
    *   **`roll_command`**:  Tercih ettiğiniz **Mudae çekme komutu** (örneğin, `wa`, `wg`, `ha`, `hg`, `w`, `h`). 🎲
    *   **`delay_seconds`**:  Bot işlemleri arasında **saniye cinsinden gecikme**. **Güvenlik için 0.8'in üzerinde tutun!** 🐢💨
    *   **`mudae_prefix`**:  **Mudae botunun ön eki** (genellikle `$`). 💰
    *   **`min_kakera`**:  Karakter almak için **minimum kakera değeri**. Her şeyi almak için `0`! 💎
    *   **`key_mode`**:  `true` veya `false`. **Kakera Anahtar Modu** için `true` - alma hakları kapalı olsa bile sürekli kakera çekimi! 🔑

4.  **🚀 Botu Çalıştırın!** Terminalinizi/komut isteminizi açın, botun klasörüne gidin ve şunu yazın:

    ```bash
    python mudae_bot.py
    ```

5.  **🕹️ İnteraktif Menü - Botlarınızı Seçin!**  Komut dosyası başlar ve bir menü sunar!

    *   Gezinmek için **↑ ve ↓ ok tuşlarını** kullanın.
    *   **"Ön Ayarı Seç ve Çalıştır"**: **Bir** bot ön ayarını çalıştırın. `presets.json` dosyanızdan seçin.
    *   **"Birden Fazla Ön Ayarı Seç ve Çalıştır"**: **Aynı anda birden fazla** bot çalıştırın! Ön ayarları **seçmek/seçimi kaldırmak için boşluk çubuğunu**, ardından **onaylamak için Enter tuşunu** kullanın. 👯‍♀️👯‍♂️
    *   **"Çıkış"**: Komut dosyasını kapatın. 👋

---

## 🎮  Çekme Zamanı! Kullanım Talimatları - Tokeninizi Alın! 🔑

1.  **🔑 Gizli Discord Tokeninizi Alın:**

    *   **DİSCORD'U WEB TARAYICINIZDA AÇIN!** (Chrome, Firefox, Safari vb.) **MASAÜSTÜ UYGULAMASI DEĞİL!** 🌐
    *   **Geliştirici Araçlarını** açmak için **F12 tuşuna basın** (veya sağ tıklayıp -> "İncele"). 👨‍💻
    *   **"Konsol"** sekmesine gidin. 💻
    *   **Bu JavaScript kodunu konsola yapıştırın ve Enter tuşuna basın:**

    ```javascript
    window.webpackChunkdiscord_app.push([
      [Math.random()],
      {},
      req => {
        if (!req.c) return;
        for (const m of Object.keys(req.c)
          .map(x => req.c[x].exports)
          .filter(x => x)) {
          if (m.default && m.default.getToken !== undefined) {
            return copy(m.default.getToken());
          }
          if (m.getToken !== undefined) {
            return copy(m.getToken());
          }
        }
      },
    ]);
    console.log('%cWorked!', 'font-size: 50px');
    console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
    ```

    *   Konsolda "%cWorked!" ve "%cYou now have your token in the clipboard!" mesajlarını göreceksiniz. 🎉
    *   **Discord tokeniniz şimdi kopyalandı!**  **`presets.json` dosyanızdaki `token` alanına YAPIŞTIRIN!** 📝

    **🔒  TOKEN GÜVENLİĞİ HER ŞEYDEN ÖNEMLİDİR! 🔒  Tokeninizi SÜPER GİZLİ BİR ŞİFRE gibi saklayın!  HİÇ KİMSEYLE PAYLAŞMAYIN!  Tokeninizi paylaşmak, Discord hesabınıza tam erişim sağlar!** 🛡️

2.  **`presets.json` dosyasını yapılandırın:**  `presets.json` dosyanızı tokenler, kanal kimlikleri, çekme komutları, gecikmeler vb. ile doldurun. Ayrıntılar için "Kurulum" bölümüne bakın. 📝

3.  **`mudae_bot.py` dosyasını çalıştırın:**  Botu terminalinizden başlatın. 🚀

4.  **Menüden Ön Ayarları Seçin:** Hangi bot ön ayarlarını çalıştırmak istediğinizi seçmek için interaktif menüyü kullanın. 🕹️

5.  **👁️ Konsolu İzleyin:**  Gerçek zamanlı bot etkinliği, günlükler ve alınan karakterler için konsolu gözünüzün önünde tutun! 👀

6.  **📜 Günlük Kaydı:**  Bot etkinliği konsol çıktısına kaydedilir. Gerekirse günlükleri kaydetmek için kopyalayıp yapıştırın. ✍️

---

## 🤝  Topluluğa Katılın! Katkılar Bekleniyor! 🤝

Mudae Otomatik Karakter Alma Botunu daha da iyi hale getirmek ister misiniz? Katkılar çok takdir edilmektedir! İyileştirme, hata düzeltmeleri veya yeni özellikler için önerileriniz mi var? İşbirliği yapalım!

*   **🐞 Sorunları Açın:** Hataları bildirin, yeni özellikler önerin, olası iyileştirmeleri tartışın!
*   **🛠️ Çekme İstekleri Gönderin:** Kod değişikliklerine katkıda bulunun! Lütfen değişikliklerinizin net açıklamalarını sağlayın.

**🙏  Lütfen bu botu sorumlu ve etik bir şekilde kullanmayı unutmayın. Discord Hizmet Şartlarına dikkat edin ve saygı gösterin. 🙏**

**Mutlu Mudae'ler! (Ama dikkatli olun!)** 😉
