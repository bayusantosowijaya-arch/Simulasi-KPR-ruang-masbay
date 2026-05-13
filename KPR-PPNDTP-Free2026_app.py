import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Ruang Masbay Property Intelegent 2026", layout="wide")

st.markdown("""
    <style>
        .block-container { padding: 0rem; }
        iframe { border: none; }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #f8fafc; margin: 0; }
        .luxury-card { background: white; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.02); border: 1px solid #f1f5f9; }
        .dark-card { background: #0f172a; color: white; border-radius: 24px; }
        .input-premium { width: 100%; border-bottom: 2px solid #e2e8f0; padding: 10px 0; font-size: 1.2rem; font-weight: 700; outline: none; transition: 0.3s; background: transparent; }
        .input-premium:focus { border-color: #0f172a; }
        .label-style { font-size: 10px; font-weight: 800; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.05em; }
        .marquee-container { overflow: hidden; background: #0f172a; padding: 10px 0; }
        .marquee-text { white-space: nowrap; display: inline-block; animation: marquee 25s linear infinite; font-size: 12px; font-weight: 700; color: #f8fafc; text-transform: uppercase; letter-spacing: 2px; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    </style>
</head>
<body>
    <div id="login-screen" class="fixed inset-0 z-50 flex items-center justify-center bg-[#0f172a]">
        <div class="w-full max-w-md bg-white rounded-3xl p-10 text-center mx-4 shadow-2xl">
            <h1 class="text-2xl font-black text-slate-900 tracking-tight">RUANG MASBAY</h1>
            <p class="text-xs text-slate-400 mb-8 font-bold uppercase tracking-widest">Property Intelegent 2026</p>
            <input type="password" id="passInput" placeholder="Security Code" class="w-full p-4 rounded-xl border border-slate-200 text-center outline-none mb-4">
            <button onclick="checkAuth()" class="w-full bg-[#0f172a] text-white py-4 rounded-xl font-bold hover:bg-slate-800 transition">UNLOCK SYSTEM</button>
        </div>
    </div>

    <div id="main-app" class="hidden min-h-screen pb-20">
        <nav class="bg-white border-b px-6 py-5 flex justify-between items-center sticky top-0 z-40">
            <div class="flex flex-col">
                <span class="font-black text-xl text-slate-900">RUANG MASBAY</span>
                <span class="text-[9px] font-bold text-slate-400 -mt-1 tracking-widest uppercase">Property Intelegent 2026</span>
            </div>
            <div class="text-[10px] bg-green-600 text-white px-4 py-1.5 rounded-full font-bold uppercase tracking-widest">PPN DTP READY</div>
        </nav>

        <div class="marquee-container">
            <div class="marquee-text">+++ Ruang Masbay Property Intelegent 2026 +++ Free PPN DTP 11% (< 2M Exclude) +++ Free PPN DTP 220JT (> 2M Exclude) +++ UTJ Memotong DP +++ AJB 0.5% & BPHTB 5% +++</div>
        </div>

        <div class="max-w-7xl mx-auto p-6 grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div class="lg:col-span-5 space-y-6">
                <div class="luxury-card p-8">
                    <h2 class="label-style mb-8 border-b pb-4 text-slate-900 font-black">Konfigurasi Finansial</h2>
                    <div class="space-y-8">
                        <div>
                            <label class="label-style">Harga Properti (Include PPN 11%)</label>
                            <input type="text" id="rawPriceInc" value="2.500.000.000" oninput="handleInput(this)" class="input-premium">
                            <div class="grid grid-cols-2 gap-4 mt-2">
                                <p class="text-[9px] text-slate-500 font-bold">Price Excl. PPN: <span id="labelExcPPN" class="text-slate-900">Rp 0</span></p>
                                <p class="text-[9px] text-green-600 font-bold text-right">Subsidi PPN DTP: <span id="subsidiLabel">Rp 0</span></p>
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-6">
                            <div>
                                <label class="label-style">Booking Fee (UTJ)</label>
                                <input type="text" id="rawBooking" value="25.000.000" oninput="handleInput(this)" class="input-premium">
                                <p class="text-[9px] text-blue-600 mt-1 font-bold italic">Nett (Excl. PPN 11%): <br><span id="utjNettLabel">Rp 0</span></p>
                            </div>
                            <div>
                                <label class="label-style">DP (%)</label>
                                <input type="number" id="dpPct" value="10" oninput="calculate()" class="input-premium">
                                <p id="dpNominalLabel" class="text-[9px] text-slate-900 mt-1 font-bold">Rp 0</p>
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-6">
                            <div><label class="label-style">Tenor (Tahun)</label><input type="number" id="tenor" value="20" oninput="calculate()" class="input-premium"></div>
                            <div><label class="label-style">Suku Bunga (% P.A)</label><input type="number" id="rate" value="4.75" step="0.01" oninput="calculate()" class="input-premium"></div>
                        </div>

                        <div>
                            <label class="label-style">Estimasi Biaya Akad KPR (%)</label>
                            <input type="number" id="akadPct" value="5" oninput="calculate()" class="input-premium">
                            <p id="akadNominalLabel" class="text-[10px] text-slate-500 mt-1 font-bold italic tracking-tight"></p>
                        </div>
                    </div>
                </div>
                
                <div class="p-6 bg-slate-900 rounded-2xl shadow-xl">
                    <p class="text-[11px] text-white leading-relaxed font-medium">
                        <span class="text-yellow-400 font-black">CATATAN:</span> Nominal <b>Uang Tanda Jadi (UTJ)</b> sudah termasuk dalam komponen Harga Jual dan akan mengurangi nilai kewajiban Down Payment (DP) pembeli.
                    </p>
                </div>
            </div>

            <div class="lg:col-span-7 space-y-6">
                <div class="dark-card p-10 shadow-2xl relative overflow-hidden bg-gradient-to-br from-slate-900 to-slate-800">
                    <p class="label-style text-slate-400 mb-2 font-black tracking-widest">ESTIMASI ANGSURAN KPR /BULAN</p>
                    <h3 id="monthlyInstallment" class="text-5xl md:text-6xl font-black tracking-tighter text-white">Rp 0</h3>
                    
                    <div class="grid grid-cols-2 gap-6 mt-10 pt-8 border-t border-white/10 text-sm">
                        <div><p class="text-[10px] uppercase opacity-40 font-bold">Plafon Pinjaman</p><p id="plafon" class="text-xl font-bold text-yellow-500">Rp 0</p></div>
                        <div class="text-right"><p class="text-[10px] uppercase opacity-40 font-bold">Harga Nett (Setelah PPN DTP)</p><p id="nettPriceLabel" class="text-xl font-bold">Rp 0</p></div>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-4">
                    <div class="luxury-card p-6 border-l-8 border-blue-600">
                        <p class="label-style mb-1">Estimasi AJB (0.5%)</p>
                        <p id="resAJB" class="text-xl font-bold text-slate-800">Rp 0</p>
                    </div>
                    <div class="luxury-card p-6 border-l-8 border-blue-600">
                        <p class="label-style mb-1">Estimasi BPHTB (5%)</p>
                        <p id="resBPHTB" class="text-xl font-bold text-slate-800">Rp 0</p>
                    </div>
                </div>

                <div class="luxury-card overflow-hidden h-[400px] flex flex-col border border-slate-100">
                    <div class="p-5 border-b bg-slate-50 flex justify-between items-center">
                        <p class="label-style text-slate-900 font-black">TABEL AMORTISASI KPR (SALDO MENURUN)</p>
                    </div>
                    <div class="overflow-y-auto flex-grow">
                        <table class="w-full text-left">
                            <thead class="bg-slate-900 text-white text-[9px] uppercase sticky top-0">
                                <tr><th class="px-6 py-4">Bulan</th><th class="px-6 py-4">Pokok</th><th class="px-6 py-4 text-right">Sisa Pinjaman</th></tr>
                            </thead>
                            <tbody id="amortTable" class="divide-y divide-slate-100"></tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function checkAuth() {
            if(document.getElementById('passInput').value === "KPR2026") {
                document.getElementById('login-screen').classList.add('hidden');
                document.getElementById('main-app').classList.remove('hidden');
                calculate();
            }
        }
        function formatNumber(n) { return n.replace(/\\D/g, "").replace(/\\B(?=(\\d{3})+(?!\\d))/g, "."); }
        function parseNumber(s) { return parseFloat(s.replace(/\\./g, "")) || 0; }
        function formatIDR(val) { return "Rp " + new Intl.NumberFormat('id-ID', { maximumFractionDigits: 0 }).format(val); }
        function handleInput(el) { el.value = formatNumber(el.value); calculate(); }

        function calculate() {
            const priceInc = parseNumber(document.getElementById('rawPriceInc').value);
            const utjRaw = parseNumber(document.getElementById('rawBooking').value);
            const dpPct = parseFloat(document.getElementById('dpPct').value) || 0;
            const tenor = parseFloat(document.getElementById('tenor').value) || 0;
            const rate = parseFloat(document.getElementById('rate').value) || 0;
            const akadPct = parseFloat(document.getElementById('akadPct').value) || 0;

            // Dasar Harga Exclude PPN
            const priceExc = priceInc / 1.11;
            document.getElementById('labelExcPPN').innerText = formatIDR(priceExc);

            // Logika PPN DTP diberikan kepada Harga Exclude
            let subsidiPPN = (priceExc < 2000000000) ? (priceExc * 0.11) : 220000000;
            const nettPrice = priceInc - subsidiPPN;
            
            // Perhitungan UTJ Nett (Potong PPN 11%)
            const utjNett = utjRaw / 1.11;
            
            // DP & Plafon
            const dpNominal = nettPrice * (dpPct / 100);
            const plafon = nettPrice - dpNominal;
            const akadCost = plafon * (akadPct / 100);
            
            const r = (rate / 100) / 12;
            const n = tenor * 12;
            const monthly = r > 0 ? plafon * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1) : plafon/n;

            // UI Update
            document.getElementById('subsidiLabel').innerText = formatIDR(subsidiPPN);
            document.getElementById('utjNettLabel').innerText = formatIDR(utjNett);
            document.getElementById('dpNominalLabel').innerText = "Nominal DP: " + formatIDR(dpNominal);
            document.getElementById('akadNominalLabel').innerText = "Est. Biaya Bank: " + formatIDR(akadCost);
            document.getElementById('nettPriceLabel').innerText = formatIDR(nettPrice);
            document.getElementById('plafon').innerText = formatIDR(plafon);
            document.getElementById('monthlyInstallment').innerText = formatIDR(monthly);
            
            // Biaya Surat-Surat (AJB & BPHTB)
            document.getElementById('resAJB').innerText = formatIDR(nettPrice * 0.005);
            document.getElementById('resBPHTB').innerText = formatIDR(nettPrice * 0.05);

            let tableHTML = "";
            let balance = plafon;
            for(let i=1; i<=n; i++) {
                let interestBln = balance * r;
                let principalBln = monthly - interestBln;
                balance -= principalBln;
                if(i <= 360) {
                    tableHTML += `<tr class="hover:bg-slate-50"><td class="px-6 py-3 font-bold text-slate-400 text-[10px]">${i}</td><td class="px-6 py-3 text-slate-600 text-[10px]">${formatIDR(principalBln)}</td><td class="px-6 py-3 text-right font-bold text-slate-900 text-[10px]">${formatIDR(Math.max(0, balance))}</td></tr>`;
                }
            }
            document.getElementById('amortTable').innerHTML = tableHTML;
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=1600, scrolling=True)
