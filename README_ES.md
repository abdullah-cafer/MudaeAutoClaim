# 💖✨ Bot de Auto-Reclamo de Mudae ✨💖

[![Violación de los TOS de Discord - **¡USA CON EXTREMA PRECAUCIÓN!**](https://img.shields.io/badge/Discord%20TOS-VIOLACIÓN-red)](https://discord.com/terms) ⚠️ **¡RIESGO DE BANN DE CUENTA!** ⚠️

**🛑🛑🛑  ¡DETENTE! LEE ESTA ** **ADVERTENCIA CRÍTICA** **ANTES DE CONTINUAR!** 🛑🛑🛑

Este bot es un **BOT PERSONAL (SELF-BOT)**. El uso de bots personales está **ESTRICTAMENTE PROHIBIDO** por Discord y **VIOLA sus Términos de Servicio**.

**🔥  CORRES EL RIESGO DE SUSPENSIÓN PERMANENTE O BANN DE TU CUENTA DE DISCORD SI USAS ESTE BOT. 🔥**

**😱  NO SOMOS RESPONSABLES DE NINGUNA ACCIÓN DE CUENTA TOMADA EN TU CONTRA POR DISCORD.  😱**

**⚠️  ¡USA ESTE BOT BAJO TU PROPIO RIESGO! PROCEDE CON EXTREMA PRECAUCIÓN Y SOLO SI ENTIENDES COMPLETAMENTE LOS PELIGROS.  ⚠️**

---

## 🚀 ¡Libera el Poder de la Automatización en Mudae! (¡Responsablemente!) 🚀

¡El **Bot de Auto-Reclamo de Mudae** es tu asistente con tecnología Python para automatizar tareas en el popular bot de Discord Mudae! ¡Optimiza tu colección de personajes, maximiza tus ganancias de kakera y lleva tu juego de Mudae al siguiente nivel! 🌟

**✨  Características Clave Que Hacen Brillar a Este Bot: ✨**

*   **👯‍♀️ Maestría Multi-Cuenta:**  ¡Ejecuta **múltiples cuentas de Discord simultáneamente**! ¡Administra todos tus esfuerzos de Mudae desde un solo script! 🚀
*   **🤖 Reclamo y Tirada Totalmente Automatizados:**  ¡Siéntate y relájate! ¡El bot **automáticamente tira, detecta personajes y kakera reclamables, y los reclama por ti!** ✨
*   **💎 Reclamo Inteligente con Kakera:**  ¡Establece tu **valor mínimo de `kakera`**! El bot inteligentemente prioriza reclamar personajes con **alto valor de kakera** (¡o reclama todo si quieres!). 🧠
*   **🥇 Lógica de Reclamo Inteligente - ¡Maximiza Tus Ganancias!**  ¡No solo reclamar, sino **reclamar inteligentemente!** ¡El bot prioriza personajes de alto valor e incluso usa `$rt` para **segundos reclamos** cuando surge la oportunidad! 🏆
*   **🔄 ¿Restablecimiento de Tiradas? ¡No Hay Problema!**  ¿Se te acaban las tiradas? ¡El bot **automáticamente detecta el agotamiento de tiradas y espera pacientemente** el próximo restablecimiento! ⏳
*   **✅ ¿Derechos de Reclamo? ¡Siempre Bajo Control!**  ¡Sin comandos desperdiciados! El bot **verifica la disponibilidad de reclamos** antes de actuar, optimizando la eficiencia. ⚡
*   **⏱️ Retrasos Personalizables - ¡Sé Como Humano!**  Ajusta los retrasos para **imitar el comportamiento humano** y **minimizar el riesgo de limitación de velocidad**. 🤫
*   **🔑 Modo Clave - ¡Colección de Kakera con Esteroides!**  ¡Activa el "Modo Clave" y el bot **tirará incansablemente por kakera** incluso cuando los derechos de reclamo no estén disponibles! ¡Nunca dejes de coleccionar! 💰
*   **🗂️ Poder de Presets - ¡Configuración Sencilla!**  ¡Administra la configuración de **todas tus cuentas en un solo archivo `presets.json` organizado!** ¡Simplicidad en su máxima expresión! 📂
*   **📊 Monitoreo de Consola en Tiempo Real - ¡Mantente Informado!**  ¡Observa el bot en acción! **Registros y actualizaciones de estado en tiempo real** directamente en tu consola! 👀
*   **📜 Registro Detallado - ¡Lleva un Registro de Tus Tesoros!**  ¡Mantén un **registro de todas las acciones del bot y personajes reclamados**! ¡Tu historial de Mudae al alcance de tu mano! 📖

---

## 🛠️ ¡Comienza en Minutos! ¡La Instalación es Pan Comido! 💨

1.  **🐍 Potencia de Python:**  Asegúrate de tener **Python 3.8 o SUPERIOR** instalado. ¡Obtenlo de [python.org](https://www.python.org/downloads/)! 🚀

2.  **📦 Instala lo Esencial:** Abre tu terminal o símbolo del sistema y ejecuta:

    ```bash
    pip install discord.py-self inquirer
    ```

3.  **📝 Crea Tu Configuración `presets.json`:**  Crea un archivo llamado `presets.json` en la misma carpeta que `mudae_bot.py`. ¡Aquí es donde ocurre la magia! ✨

    ```json
    {
      "MiBotGenial1": {  // 🌟 ¡Dale un nombre genial a tu preset!
        "token": "TU_TOKEN_DE_CUENTA_DE_DISCORD_1",   // 🔑  ¡Tu token de cuenta secreto! (¡Mira la sección de Uso!)
        "prefix": "!",                             // ⚙️  Prefijo de comando del bot (probablemente no usarás mucho esto)
        "channel_id": 123456789012345678,         // 💬  ID del Canal de Discord - ¡donde trabaja el bot! (¡Obtenlo en Discord!)
        "roll_command": "wa",                       // 🎲  Comando de tirada de Mudae de elección (wa, wg, ha, hg, w, h)
        "delay_seconds": 1,                         // ⏳  Retraso entre acciones (segundos, ¡mantenlo por encima de 0.8 por seguridad!)
        "mudae_prefix": "$",                        // 💰  Prefijo de comando de Mudae (generalmente $)
        "min_kakera": 50,                           // 💎  Valor mínimo de kakera para reclamar personajes (0 para reclamar todo)
        "key_mode": false                           // 🔑  ¿Activar Modo Clave? (true/false - para tiradas enfocadas en Kakera)
      },
      "BotCazadorDeKakera": {   // 🚀 ¡Otro preset genial!
        "token": "TU_TOKEN_DE_CUENTA_DE_DISCORD_2",
        "prefix": "?",
        "channel_id": 987654321098765432,
        "roll_command": "wg",
        "delay_seconds": 1.5,
        "mudae_prefix": "$",
        "min_kakera": 75,
        "key_mode": true
      }
      // ... ¡Agrega más presets para todas tus cuentas! 🚀🚀🚀
    }
    ```

    **🔍  Ajustes de `presets.json` - Explicados en Detalle:**

    *   **`preset_name`**:  Un **nombre descriptivo** para tu preset (ej., "CuentaPrincipal", "BotAlternativo"). Esto te ayuda a identificar los bots en la consola.
    *   **`token`**: **¡TU TOKEN DE CUENTA DE DISCORD!** ¡Esto es **SÚPER SECRETO!** Mira la sección "Uso" a continuación para saber cómo obtenerlo. **¡NUNCA COMPARTAS TU TOKEN!** 🔒
    *   **`prefix`**:  El prefijo de comando del bot. Probablemente no usarás mucho esto, configúralo a cualquier cosa (ej., `!`, `?`, `.`).
    *   **`channel_id`**:  El **ID del Canal de Discord** donde operará el bot. **Activa el Modo de Desarrollador en Discord** (Ajustes -> Apariencia -> Avanzado), luego **haz clic derecho en el canal y selecciona "Copiar ID"**. 💬
    *   **`roll_command`**:  Tu **comando de tirada de Mudae** preferido (ej., `wa`, `wg`, `ha`, `hg`, `w`, `h`). 🎲
    *   **`delay_seconds`**:  **Retraso en segundos** entre acciones del bot. **¡Mantenlo por encima de 0.8 por seguridad!** 🐢💨
    *   **`mudae_prefix`**:  El **prefijo del bot de Mudae** (generalmente `$`). 💰
    *   **`min_kakera`**:  **Valor mínimo de kakera** para reclamar personajes. ¡`0` para reclamar todo! 💎
    *   **`key_mode`**:  `true` o `false`. `true` para **Modo Clave de Kakera** - ¡tiradas continuas de kakera incluso cuando los derechos de reclamo están inactivos! 🔑

4.  **🚀 ¡Ejecuta el Bot!** Abre tu terminal/símbolo del sistema, navega a la carpeta del bot y escribe:

    ```bash
    python mudae_bot.py
    ```

5.  **🕹️ Menú Interactivo - ¡Elige Tus Bots!**  ¡El script comienza y presenta un menú!

    *   Usa las **teclas de flecha ↑ y ↓** para navegar.
    *   **"Select and Run Preset"**: Ejecuta **un** preset de bot. Elige de tu `presets.json`.
    *   **"Select and Run Multiple Presets"**: ¡Ejecuta **múltiples** bots a la vez! ¡Usa la **barra espaciadora para seleccionar/deseleccionar** presets, luego **Enter para confirmar**. 👯‍♀️👯‍♂️
    *   **"Exit"**: Cierra el script. 👋

---

## 🎮  ¡Hora de Tirar los Dados! Instrucciones de Uso - ¡Obtén Tu Token! 🔑

1.  **🔑 Obtén Tu Token Secreto de Discord:**

    *   **¡ABRE DISCORD EN TU NAVEGADOR WEB!** (Chrome, Firefox, Safari, etc.) **¡NO LA APLICACIÓN DE ESCRITORIO!** 🌐
    *   **Presiona F12** para abrir las **Herramientas de Desarrollador** (o haz clic derecho -> "Inspeccionar"). 👨‍💻
    *   Ve a la pestaña **"Consola"**. 💻
    *   **Pega este código JavaScript en la consola y presiona Enter:**

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

    *   Verás "%cWorked!" y "%cYou now have your token in the clipboard!". 🎉
    *   **¡Tu token de Discord ahora está copiado!**  **¡PÉGALO en el campo `token` en tu archivo `presets.json`!** 📝

    **🔒  ¡LA SEGURIDAD DEL TOKEN ES PRIMORDIAL! 🔒  ¡Trata tu token como una CONTRASEÑA SÚPER SECRETA!  ¡NO LO COMPARTAS CON NADIE!  ¡Compartir tu token da acceso completo a tu cuenta de Discord!** 🛡️

2.  **Configura `presets.json`:**  Llena tu archivo `presets.json` con tokens, IDs de canal, comandos de tirada, retrasos, etc.  Consulta la sección "Instalación" para obtener detalles. 📝

3.  **Ejecuta `mudae_bot.py`:**  Inicia el bot desde tu terminal. 🚀

4.  **Selecciona Presets del Menú:** Usa el menú interactivo para elegir qué presets de bot ejecutar. 🕹️

5.  **👁️ Monitorea la Consola:**  ¡Vigila la consola para ver la actividad del bot en tiempo real, los registros y los personajes reclamados! 👀

6.  **📜 Registro:**  La actividad del bot se registra en la salida de la consola. Copia y pega para guardar los registros si es necesario. ✍️

---

## 🤝  ¡Únete a la Comunidad! ¡Las Contribuciones Son Bienvenidas! 🤝

¿Quieres hacer que el Bot de Auto-Reclamo de Mudae sea aún mejor? ¡Las contribuciones son muy apreciadas! ¿Tienes ideas, correcciones de errores o nuevas características? ¡Colaboremos!

*   **🐞 Abre Issues:** ¡Reporta errores, sugiere características, discute mejoras!
*   **🛠️ Envía Pull Requests:**  ¡Contribuye con cambios de código!  Por favor, proporciona descripciones claras de tus cambios.

**🙏  Recuerda usar este bot de manera responsable y ética.  Sé consciente y respeta los Términos de Servicio de Discord. 🙏**

**¡Felices Mudaeos! (¡Pero ten cuidado!)** 😉
