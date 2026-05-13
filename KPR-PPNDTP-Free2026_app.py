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
        body { font-family: 'Inter', sans-serif; background: #f1f5f9; margin: 0; overflow-x: hidden; }
        .luxury-card { background: white; border-radius: 20px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); border: 1px solid #e2e8f0; }
        .dark-card { background: #0f172a; color: white; border-radius: 20px; }
        .input-premium { width: 100%; border-bottom: 2px solid #e2e8f0; padding: 8px 0; font-size: 1.1rem; font-weight: 700; outline: none; transition: 0.3s; background: transparent; }
        .input-premium:focus { border-color: #0f172a; }
        .label-style { font-size: 10px; font-weight: 800; text-transform: uppercase; color: #64748b; letter-spacing: 0.05em; }
        .highlight-gold { color: #eab308; }
        .marquee-container { overflow: hidden; background: #0f172a; padding: 8px 0; display: none; }
        .marquee-text { white-space: nowrap; display: inline-block; animation: marquee 30s linear infinite; font-size: 12px; font-weight: 700; color: #f8fafc; text-transform: uppercase; letter-spacing: 2px; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    </style>
</head>
<body>
    <div id="login-screen" class="fixed inset-0 z-50 flex items-center justify-center bg-[#0f172a]">
        <div class="w-full max-w-md bg-white rounded-3xl p-10 text-center mx-4 shadow-2xl">
            <h1 class="text-2xl font-black text-slate-900 tracking-tight">RUANG MASBAY</h1>
            <p class="text-xs text-slate-400 mb-8 font-bold uppercase tracking-widest">Property Intelegent 2026</p>
            <input type="password" id="passInput" placeholder="Security Code" class="w-full p-4 rounded-xl border border-slate-200 text-center outline-none focus:ring-2 focus:ring-slate-900 mb-4">
            <button onclick="checkAuth()" class="w-full bg-[#0f172a] text-white py-4 rounded-xl font-bold hover:bg-slate-800 transition">UNLOCK SYSTEM</button>
        </div>
    </div>
    <div id="main-app" class="hidden min-h-screen">
        <nav class="bg-white border-b px-6 py-4 flex justify-between items-center sticky top-0 z-40">
            <div class="flex flex-col">
                <span class="font-black text-lg text-slate-900">RUANG MASBAY</span>
                <span class="text-[9px] font-bold text-slate-400 -mt-1 tracking-widest uppercase">Property Intelegent 2026</span>
            </div>
            <div class="text-[10px] bg-green-600 text-white px-3 py-1 rounded-full font-bold uppercase tracking-tighter">PPN DTP Calculator V2</div>
        </nav>
        <div id="marquee" class="marquee-container">
            <div class="marquee-text">+++ Ruang Masbay Property Intelegent 2026 +++ Free PPN DTP 11% (Exclude PPN < 2M) +++ Free PPN DTP 220JT (Exclude PPN > 2M) +++ AJB 0.5% & BPHTB 5% Included +++ Amortisasi up to 30 Tahun +++</div>
        </div>
        <div class="max-w-7xl mx-auto p-4 md:p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
            <div class="lg:col-span-4 space-y-6">
                <div class="luxury-card p-6">
                    <h2 class="label-style mb-6 border-b pb-2 text-slate-900">Input Data Properti</h2>
                    <div class="space-y-6">
                        <div>
                            <label class="label-style">Harga Properti (Inc. PPN 11%)</label>
                            <div class="flex items-center border-b-2 border-slate-200 focus-within:border-slate-900 transition">
                                <span class="text-lg font-bold text-slate-400 mr-2">Rp</span>
                                <input type="text" id="rawPriceInc" value="2.500.000.000" oninput="handleInput(this)" class="w-full p-2 text-xl font-bold outline-none bg-transparent">
                            </div>
                            <div class="mt-2 text-[10px] text-slate-500 font-bold">Harga Exclude PPN: <span id="labelExcPPN" class="text-slate-900">Rp 0</span></div>
                        </div>
                        <div class="grid grid-cols-2 gap-4">
                            <div><label class="label-style">Booking Fee (UTJ)</label><input type="text" id="rawBooking" value="25.000.000" oninput="handleInput(this)" class="input-premium"></div>
                            <div><label class="label-style">DP (%)</label><input type="number" id="dpPct" value="10" oninput="calculate()" class="input-premium"></div>
                        </div>
                        <div class="grid grid-cols-2 gap-4">
                            <div><label class="label-style">Tenor (Thn)</label><input type="number" id="tenor" value="20" max="30" oninput="calculate()" class="input-premium"></div>
                            <div><label class="label-style">Bunga (%)</label><input type="number" id="rate" value="4.75" step="0.01" oninput="calculate()" class="input-premium"></div>
                        </div>
                    </div>
                </div>
                <div class="luxury-card p-6 bg-slate-50">
                    <h2 class="label-style mb-4 text-slate-900">Estimasi Biaya Legal</h2>
                    <div class="space-y-4">
                        <div class="flex justify-between border-b border-slate-200 pb-2">
                            <span class="text-[10px] font-bold text-slate-500 uppercase">AJB (0.5%)</span>
                            <span id="resAJB" class="text-sm font-bold text-slate-800">Rp 0</span>
                        </div>
                        <div class="flex justify-between border-b border-slate-200 pb-2">
                            <span class="text-[10px] font-bold text-slate-500 uppercase">BPHTB (5%)</span>
                            <span id="resBPHTB" class="text-sm font-bold text-slate-800">Rp 0</span>
                        </div>
                        <div class="flex justify-between pt-2">
                            <span class="text-[10px] font-black text-slate-900 uppercase">Total Legal</span>
                            <span id="resTotalLegal" class="text-sm font-black text-blue-700">Rp 0</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="lg:col-span-8 space-y-6">
                <div class="dark-card p-8 md:p-10 shadow-2xl bg-gradient-to-br from-slate-900 to-slate-800 border-b-4 border-yellow-500">
                    <p class="label-style text-slate-400 mb-2 font-black tracking-widest">ESTIMASI ANGSURAN PER BULAN</p>
                    <h3 id="monthlyInstallment" class="text-4xl md:text-6xl font-black tracking-tighter text-white">Rp 0</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8 pt-8 border-t border-white/10">
                        <div><p class="text-[9px] uppercase opacity-50 font-bold mb-1">Subsidi PPN DTP</p><p id="subsidiLabel" class="text-lg font-bold text-green-400">Rp 0</p></div>
                        <div><p class="text-[9px] uppercase opacity-50 font-bold mb-1">Plafon KPR</p><p id="plafon" class="text-lg font-bold highlight-gold">Rp 0</p></div>
                        <div class="md:text-right"><p class="text-[9px] uppercase opacity-50 font-bold mb-1">Harga Nett Properti</p><p id="nettPriceLabel" class="text-lg font-bold">Rp 0</p></div>
                    </div>
                </div>
                <div class="luxury-card overflow-hidden h-[450px] flex flex-col">
                    <div class="p-4 border-b bg-slate-50 font-black text-[10px] tracking-widest text-slate-900 uppercase">Schedule Amortisasi (Full Tenor)</div>
                    <div class="overflow-y-auto flex-grow">
                        <table class="w-full text-left border-collapse">
                            <thead class="bg-slate-900 text-white text-[9px] uppercase sticky top-0">
                                <tr><th class="px-4 py-3">Bulan</th><th class="px-4 py-3">Pokok</th><th class="px-4 py-3">Bunga</th><th class="px-4 py-3 text-right">Sisa Pinjaman</th></tr>
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
            if(document.getElementById('passInput').value === "RuangMasbay2026") {
                document.getElementById('login-screen').classList.add('hidden');
                document.getElementById('main-app').classList.remove('hidden');
                document.getElementById('marquee').style.display = 'block';
                calculate();
            }
        }
        function formatNumber(n) { return n.replace(/\\D/g, "").replace(/\\B(?=(\\d{3})+(?!\\d))/g, "."); }
        function parseNumber(s) { return parseFloat(s.replace(/\\./g, "")) || 0; }
        function formatIDR(val) { return "Rp " + new Intl.NumberFormat('id-ID', { maximumFractionDigits: 0 }).format(val); }
        function handleInput(el) { el.value = formatNumber(el.value); calculate(); }
        function calculate() {
            const priceInc = parseNumber(document.getElementById('rawPriceInc').value);
            const dpPct = parseFloat(document.getElementById('dpPct').value) || 0;
            const tenor = parseFloat(document.getElementById('tenor').value) || 0;
            const rate = parseFloat(document.getElementById('rate').value) || 0;
            const priceExc = priceInc / 1.11;
            document.getElementById('labelExcPPN').innerText = formatIDR(priceExc);
            let subsidiPPN = (priceExc < 2000000000) ? (priceExc * 0.11) : 220000000;
            const nettPrice = priceInc - subsidiPPN;
            const ajb = nettPrice * 0.005;
            const bphtb = nettPrice * 0.05;
            const dpNominal = nettPrice * (dpPct / 100);
            const plafon = nettPrice - dpNominal;
            const r = (rate / 100) / 12;
            const n = Math.min(tenor, 30) * 12;
            const monthly = r > 0 ? plafon * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1) : plafon/n;
            document.getElementById('subsidiLabel').innerText = formatIDR(subsidiPPN);
            document.getElementById('nettPriceLabel').innerText = formatIDR(nettPrice);
            document.getElementById('plafon').innerText = formatIDR(plafon);
            document.getElementById('monthlyInstallment').innerText = formatIDR(monthly);
            document.getElementById('resAJB').innerText = formatIDR(ajb);
            document.getElementById('resBPHTB').innerText = formatIDR(bphtb);
            document.getElementById('resTotalLegal').innerText = formatIDR(ajb + bphtb);
            let tableHTML = "";
            let balance = plafon;
            for(let i=1; i<=n; i++) {
                let interestBln = balance * r;
                let principalBln = monthly - interestBln;
                balance -= principalBln;
                tableHTML += `<tr class="text-[10px] hover:bg-slate-50"><td class="px-4 py-2 font-bold text-slate-400">${i}</td><td class="px-4 py-2">${formatIDR(principalBln)}</td><td class="px-4 py-2 text-red-400">${formatIDR(interestBln)}</td><td class="px-4 py-2 text-right font-bold">${formatIDR(Math.max(0, balance))}</td></tr>`;
            }
            document.getElementById('amortTable').innerHTML = tableHTML;
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=1200, scrolling=True)
