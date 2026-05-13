import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Ruang Masbay Property Intelegent", layout="wide")

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
        body { font-family: 'Inter', sans-serif; background: #f8fafc; margin: 0; overflow-x: hidden; }
        .luxury-card { background: white; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.02); border: 1px solid #f1f5f9; }
        .dark-card { background: #0f172a; color: white; border-radius: 24px; }
        .input-premium { width: 100%; border-bottom: 2px solid #e2e8f0; padding: 10px 0; font-size: 1.25rem; font-weight: 700; outline: none; transition: 0.3s; background: transparent; }
        .input-premium:focus { border-color: #0f172a; }
        .label-style { font-size: 11px; font-weight: 800; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.05em; }
        .highlight-gold { color: #eab308; }
        
        .marquee-container {
            overflow: hidden;
            background: #0f172a;
            padding: 10px 0;
            display: none;
        }
        .marquee-text {
            white-space: nowrap;
            display: inline-block;
            animation: marquee 25s linear infinite;
            font-size: 13px;
            font-weight: 700;
            color: #f8fafc;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
    </style>
</head>
<body>

    <div id="login-screen" class="fixed inset-0 z-50 flex items-center justify-center bg-[#0f172a]">
        <div class="w-full max-w-md bg-white rounded-3xl p-10 text-center mx-4 shadow-2xl border border-slate-100">
            <h1 class="text-2xl font-bold text-slate-900 tracking-tight uppercase">Ruang Masbay</h1>
            <p class="text-sm text-slate-400 mb-8 mt-1 font-medium italic">Property Intelegent 2026</p>
            <input type="password" id="passInput" placeholder="Masukan Kode Keamanan" 
            class="w-full p-4 rounded-xl border border-slate-200 text-center outline-none focus:ring-2 focus:ring-slate-900 transition-all mb-4">
            <button onclick="checkAuth()" class="w-full bg-[#0f172a] text-white py-4 rounded-xl font-bold hover:bg-slate-800 transition shadow-lg">UNLOCK SYSTEM</button>
        </div>
    </div>

    <div id="main-app" class="hidden min-h-screen pb-20">
        <nav class="bg-white border-b px-6 py-5 flex justify-between items-center sticky top-0 z-40">
            <div class="flex flex-col">
                <span class="font-black tracking-tighter text-xl text-slate-900 uppercase">RUANG MASBAY</span>
                <span class="text-[9px] font-bold text-slate-400 -mt-1 tracking-[0.2em]">INTELEGENT SIMULATOR 2026</span>
            </div>
            <div class="text-[10px] bg-green-600 text-white px-4 py-1.5 rounded-full font-bold uppercase tracking-widest shadow-sm">FREE PPN ACTIVE</div>
        </nav>

        <div id="marquee" class="marquee-container">
            <div class="marquee-text">
                +++ Ruang Masbay 2026 Property Intelegent +++ Free PPN 11% (< 2M) & Free PPN 220JT (> 2M) +++ UTJ Termasuk Harga & Free PPN 11% Applied +++
            </div>
        </div>

        <div class="max-w-6xl mx-auto p-6 mt-4 grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div class="lg:col-span-5 space-y-6">
                <div class="luxury-card p-8">
                    <h2 class="label-style mb-8 border-b pb-4 text-slate-900 font-black">Input Penawaran</h2>
                    <div class="space-y-8">
                        <div>
                            <label class="label-style">Harga Properti (Inc. PPN)</label>
                            <div class="flex items-center border-b-2 border-slate-200 focus-within:border-slate-900 transition">
                                <span class="text-xl font-bold text-slate-400 mr-2">Rp</span>
                                <input type="text" id="rawPriceInc" value="2.500.000.000" oninput="handleInput(this)" class="w-full p-2 text-2xl font-bold outline-none bg-transparent">
                            </div>
                            <div class="mt-3 p-3 bg-green-50 rounded-lg border border-green-100">
                                <p class="text-[10px] text-green-700 font-bold">ESTIMASI SUBSIDI PPN DTP:</p>
                                <p id="subsidiLabel" class="text-sm font-black text-green-800">Rp 0</p>
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-6">
                            <div>
                                <label class="label-style">Uang Tanda Jadi (UTJ)</label>
                                <input type="text" id="rawBooking" value="25.000.000" oninput="handleInput(this)" class="input-premium">
                                <p class="text-[10px] font-bold text-blue-600 mt-2">Nett (Free PPN): <span id="utjNettLabel">Rp 0</span></p>
                            </div>
                            <div>
                                <label class="label-style">DP (%)</label>
                                <input type="number" id="dpPct" value="10" oninput="calculate()" class="input-premium">
                                <p id="dpNominal" class="text-[10px] font-bold text-slate-500 mt-1">Rp 0</p>
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-6">
                            <div><label class="label-style">Tenor (Tahun)</label><input type="number" id="tenor" value="15" oninput="calculate()" class="input-premium"></div>
                            <div><label class="label-style">Bunga (%)</label><input type="number" id="rate" value="4.75" step="0.01" oninput="calculate()" class="input-premium"></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="lg:col-span-7 space-y-6">
                <div class="dark-card p-10 shadow-2xl relative overflow-hidden bg-gradient-to-br from-slate-900 to-slate-800">
                    <p class="label-style text-slate-500 mb-2 font-black tracking-widest text-xs">ESTIMASI ANGSURAN / BULAN</p>
                    <h3 id="monthlyInstallment" class="text-5xl md:text-6xl font-black tracking-tighter text-white">Rp 0</h3>
                    <div class="grid grid-cols-2 gap-6 mt-10 pt-8 border-t border-white/10">
                        <div><p class="text-[10px] uppercase opacity-40 font-bold">Plafon KPR</p><p id="plafon" class="text-xl font-bold highlight-gold">Rp 0</p></div>
                        <div class="text-right"><p class="text-[10px] uppercase opacity-40 font-bold">Harga Nett (Setelah Subsidi)</p><p id="valInc" class="text-xl font-bold">Rp 0</p></div>
                    </div>
                </div>
                <div class="luxury-card p-6 border-l-8 border-blue-900">
                    <p class="text-[12px] font-medium text-slate-600 italic">"Nilai UTJ sudah termasuk dalam harga dan memotong kewajiban pelunasan konsumen."</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        function checkAuth() {
            if(document.getElementById('passInput').value === "RuangMasbay2026") {
                document.getElementById('login-screen').classList.add('hidden');
                document.getElementById('main-app').classList.remove('hidden');
                document.getElementById('marquee').style.display = 'block';
                calculate();
            }
        }

        function formatNumber(n) { return n.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, "."); }
        function parseNumber(s) { return parseFloat(s.replace(/\./g, "")) || 0; }
        function formatIDR(val) { return "Rp " + new Intl.NumberFormat('id-ID', { maximumFractionDigits: 0 }).format(val); }

        function handleInput(el) {
            el.value = formatNumber(el.value);
            calculate();
        }

        function calculate() {
            const priceInc = parseNumber(document.getElementById('rawPriceInc').value);
            const utjRaw = parseNumber(document.getElementById('rawBooking').value);
            const dpPct = parseFloat(document.getElementById('dpPct').value) || 0;
            const tenor = parseFloat(document.getElementById('tenor').value) || 0;
            const rate = parseFloat(document.getElementById('rate').value) || 0;

            let subsidiPPN = (priceInc < 2000000000) ? (priceInc - (priceInc / 1.11)) : 220000000;
            const nettPrice = priceInc - subsidiPPN;
            const utjNett = utjRaw / 1.11;
            const dpNominal = nettPrice * (dpPct / 100);
            const plafon = nettPrice - dpNominal;
            const r = (rate / 100) / 12;
            const n = tenor * 12;
            const monthly = r > 0 ? plafon * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1) : plafon/n;

            document.getElementById('subsidiLabel').innerText = formatIDR(subsidiPPN);
            document.getElementById('utjNettLabel').innerText = formatIDR(utjNett);
            document.getElementById('valInc').innerText = formatIDR(nettPrice);
            document.getElementById('monthlyInstallment').innerText = formatIDR(monthly);
            document.getElementById('plafon').innerText = formatIDR(plafon);
            document.getElementById('dpNominal').innerText = "Potongan DP dari UTJ: " + formatIDR(dpNominal);
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=1200, scrolling=True)
