import { ref } from "vue"
import api from "@/services/api"

export function koristiGlasovnoPopunjavanje() {
  const snimam = ref(false)
  const obradaUTijeku = ref(false)
  const tekstGumba = ref("Ispunite glasovno pomoću AI")
  const klasaGumba = ref("")
  const greska = ref(null)

  const zadnjiTranskript = ref("")

  let snimacGlasa = null
  let dijeloviSnimke = []
  let tokMikrofona = null

  function ugasiMikrofon() {
    try {
      tokMikrofona?.getTracks()?.forEach((t) => t.stop())
    } catch {}
    tokMikrofona = null
  }

  function resetirajUI() {
    snimam.value = false
    tekstGumba.value = "Ispunite glasovno pomoću AI"
    klasaGumba.value = ""
  }

  async function zapocniSnimanje() {
    try {
      greska.value = null
      zadnjiTranskript.value = ""
      const pristupMikrofonuKorisnika = await navigator.mediaDevices.getUserMedia({ audio: true })
      tokMikrofona = pristupMikrofonuKorisnika
      dijeloviSnimke = []
      snimacGlasa = new MediaRecorder(pristupMikrofonuKorisnika, { mimeType: "audio/webm" })
      snimacGlasa.ondataavailable = (e) => e.data?.size > 0 && dijeloviSnimke.push(e.data)
      snimacGlasa.start()
      snimam.value = true
      tekstGumba.value = "Snimanje u tijeku..."
      klasaGumba.value = "animate-bounce"
      zadnjiTranskript.value = "Slušam..."
    } catch (e) {
      console.error(e)
      greska.value = "Mikrofon nije dostupan ili je odbijen pristup."
      ugasiMikrofon()
      resetirajUI()
    }
  }

  async function zaustaviSnimanjeIVratiTranskript() {
    return new Promise((resolve) => {
      if (!snimacGlasa || snimacGlasa.state === "inactive") {
        ugasiMikrofon()
        resetirajUI()
        resolve({ ok: false, tekst: "" })
        return
      }
      snimacGlasa.onstop = async () => {
        try {
          snimam.value = false
          obradaUTijeku.value = true
          tekstGumba.value = "Dohvaćam podatke iz snimke…"
          klasaGumba.value = ""

          const blob = new Blob(dijeloviSnimke, { type: "audio/webm" })
          const fd = new FormData()
          fd.append("audio", blob, "snimka.webm")

          const transkribiraj = await api.post("/ai/transkribiraj", fd, {
            headers: { "Content-Type": "multipart/form-data" },
          })

          const tekst = transkribiraj?.data?.tekst || ""

          zadnjiTranskript.value = tekst || "Nema prepoznatog teksta"

          resolve({ ok: true, tekst })
        } catch (e) {
          console.error(e)
          greska.value = "Greška pri transkripciji"
          resolve({ ok: false, tekst: "" })
        } finally {
          ugasiMikrofon()
          resetirajUI()
          snimacGlasa = null
          dijeloviSnimke = []
        }
      }
      try {
        snimacGlasa.stop()
      } catch {}
    })
  }

  async function strukturirajTekst(tekst, strukturaUpita) {
    obradaUTijeku.value = true
    tekstGumba.value = "Dohvaćam podatke iz snimke…"
    try {
      const strukturiraj = await api.post("/ai/strukturiraj", {
        tekst,
        struktura_upita: strukturaUpita,
      })
      return { ok: true, podaci: strukturiraj?.data?.podaci || {} }
    } catch (e) {
      console.error(e)
      greska.value = "Greška pri strukturiranju teksta"
      return { ok: false, podaci: {} }
    } finally {
      obradaUTijeku.value = false
      tekstGumba.value = "Ispunite glasovno pomoću AI"
    }
  }

  window.addEventListener("beforeunload", ugasiMikrofon)

  return {
    snimam,
    obradaUTijeku,
    tekstGumba,
    klasaGumba,
    greska,
    zadnjiTranskript,
    zapocniSnimanje,
    zaustaviSnimanjeIVratiTranskript,
    strukturirajTekst,
  }
}
