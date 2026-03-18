import re

css_file = '/Users/sumitkumar/Desktop/Hello/style.css'

with open(css_file, 'r') as f:
    orig_css = f.read()

# Define the CLEAN version from scratch to ensure quality
# (I will take the good parts from the existing CSS)

clean_css = """@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Inter:wght@300;400;500;600;700&display=swap');

/* ===== FOUNDATION & VARIABLES ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary-color: #1b3a2a; 
    --secondary-color: #d4af37; 
    --accent-color: #C5A059;
    --bg-color: #fdfbf7; 
    --text-color: #333333;
    --text-muted: #666666;
    --white: #ffffff;
    --black: #000000;
    --font-heading: 'Playfair Display', serif;
    --font-body: 'Inter', sans-serif;
    --container-max-width: 1200px;
    --section-padding: 80px 20px;
    --border-radius: 12px;
    --transition: all 0.3s ease;
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
    --shadow-lg: 0 10px 30px rgba(0,0,0,0.15);
}

body {
    font-family: var(--font-body);
    color: var(--text-color);
    background-color: var(--bg-color);
    line-height: 1.6;
    overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    font-weight: 700;
}

a {
    text-decoration: none;
    color: inherit;
    transition: var(--transition);
}

ul { list-style: none; }
img { max-width: 100%; display: block; }
.container { max-width: var(--container-max-width); margin: 0 auto; padding: 0 20px; }
section { padding: var(--section-padding); }

/* ===== COMPONENTS ===== */
.btn {
    display: inline-block;
    padding: 12px 28px;
    border-radius: var(--border-radius);
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition);
    border: none;
    font-size: 1rem;
    text-align: center;
}

.btn-primary {
    background-color: var(--secondary-color);
    color: var(--white);
}

.btn-primary:hover {
    background-color: var(--accent-color);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(212,175,55,0.4);
}

.btn-outline {
    background: transparent;
    border: 1px solid var(--secondary-color);
    color: var(--secondary-color);
    padding: 10px 20px;
}

.btn-outline:hover {
    background: var(--secondary-color);
    color: var(--white);
}

.glass {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title { text-align: center; margin-bottom: 50px; }
.section-title h2 { font-size: 2.5rem; color: var(--primary-color); margin-bottom: 15px; }
.section-title p { color: var(--text-muted); font-size: 1.1rem; }

/* ===== NAVIGATION (SLIM & TRANSLUCENT) ===== */
.header, .navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
    padding: 8px 0;
    background: rgba(27, 58, 42, 0.65) !important;
    backdrop-filter: blur(14px) !important;
    -webkit-backdrop-filter: blur(14px) !important;
    border-bottom: 1px solid rgba(212, 175, 55, 0.15);
}

.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
}

.logo a {
    font-family: var(--font-heading);
    font-size: 1.25rem;
    color: var(--white);
    letter-spacing: 1px;
    font-weight: 700;
}

.nav-links { display: flex; gap: 25px; }
.nav-links a { color: var(--white); font-size: 0.85rem; font-weight: 500; text-transform: uppercase; }
.nav-links a:hover, .nav-links a.active { color: var(--secondary-color); }

.mobile-menu-icon { display: none; color: var(--white); font-size: 1.5rem; cursor: pointer; }

/* ===== HERO SECTION (CLEAN) ===== */
.hero {
    position: relative;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--white);
    text-align: center;
    padding-top: 60px;
}

.hero-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    z-index: -1;
}

.hero-bg img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.5); }

.hero-title {
    font-size: 4.2rem;
    margin-bottom: 16px;
    color: #fff;
    line-height: 1.1;
    text-shadow: none;
}

.hero-description {
    font-size: 1.15rem;
    max-width: 550px;
    margin: 0 auto 35px;
    font-weight: 300;
    color: rgba(255,255,255,0.85);
}

.hero-btns { margin-bottom: 35px; }
.hero-call-btn {
    background: var(--secondary-color);
    color: var(--white);
    padding: 14px 35px;
    font-size: 1.1rem;
    display: inline-flex;
    align-items: center;
    gap: 10px;
}

/* ===== BOOKING SEARCH BAR ===== */
.booking-search {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 16px 35px;
    border-radius: 12px;
    max-width: 1050px;
    margin: 0 auto;
    background: rgba(27, 58, 42, 0.85);
    border: 1px solid rgba(212, 175, 55, 0.3);
}

.search-item { flex: 1; text-align: left; display: flex; flex-direction: column; gap: 4px; }
.search-item label { font-size: 0.75rem; color: var(--secondary-color); display: flex; align-items: center; gap: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
.search-item input { background: transparent; border: none; border-bottom: 1px solid rgba(255,255,255,0.2); color: var(--white); padding: 6px 0; outline: none; width: 100%; font-size: 0.95rem; }

.guest-counter { display: flex; align-items: center; gap: 12px; background: rgba(255, 255, 255, 0.05); padding: 4px 10px; border-radius: 4px; border: 1px solid rgba(255, 255, 255, 0.1); width: fit-content; }
.counter-btn { background: var(--secondary-color); color: var(--white); border: none; width: 24px; height: 24px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1rem; transition: var(--transition); }
.guest-counter input { width: 30px; text-align: center; background: transparent; border: none; color: var(--white); font-weight: 600; -moz-appearance: textfield; }

.search-divider { width: 1px; height: 35px; background: rgba(255,255,255,0.15); flex-shrink: 0; }
.search-btn { background: linear-gradient(135deg, var(--secondary-color), var(--accent-color)); color: white; padding: 14px 30px; border-radius: 8px; font-weight: 700; display: flex; align-items: center; gap: 8px; }

/* ===== ROOMS, SERVICES, ABOUT, GALLERY, EXPERIENCES ===== */
.grid { display: grid; gap: 30px; }
.rooms-grid { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }
.room-card { background: var(--white); border-radius: var(--border-radius); overflow: hidden; box-shadow: var(--shadow-md); position: relative; }
.room-img img { width: 100%; height: 260px; object-fit: cover; }
.room-info { padding: 25px; }
.room-price { font-size: 1.35rem; font-weight: 700; color: var(--secondary-color); margin-bottom: 8px; }
.room-badge { position: absolute; top: 15px; right: 15px; background: var(--secondary-color); color: var(--white); padding: 5px 14px; border-radius: 25px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; z-index: 5; }

.services { background: #fff; }
.services-grid { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.service-item { text-align: center; padding: 35px 25px; border: 1px solid #f0f0f0; border-radius: var(--border-radius); }
.service-icon { font-size: 2.2rem; color: var(--secondary-color); margin-bottom: 15px; }

.about { background: var(--primary-color); color: #fff; padding: 90px 0; }
.about-row { display: flex; align-items: center; gap: 60px; flex-wrap: wrap; }
.about-content, .about-img { flex: 1; min-width: 320px; }
.about-img img { border-radius: var(--border-radius); }

.gallery-grid { display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 220px); gap: 15px; }
.gallery-item { border-radius: 10px; overflow: hidden; }
.gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: var(--transition); }
.gallery-item:hover img { transform: scale(1.08); }
.gallery-item.large { grid-row: span 2; }

.experiences-grid { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.experience-card { background: #fff; padding: 20px; border-radius: 12px; text-align: center; box-shadow: var(--shadow-sm); }
.experience-card img { width: 100%; height: 210px; object-fit: cover; border-radius: 10px; margin-bottom: 20px; }

/* ===== FOOTER ===== */
.footer { background: var(--primary-color); color: #fff; padding: 80px 0 30px; }
.footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; }
.footer-info h3 { color: var(--secondary-color); margin-bottom: 20px; }
.footer-info p { color: rgba(255,255,255,0.65); font-size: 0.9rem; margin-bottom: 10px; }
.footer-info i { color: var(--secondary-color); margin-right: 8px; }
.footer-links h4 { margin-bottom: 20px; }
.footer-links ul li { margin-bottom: 10px; }
.footer-links a { color: rgba(255,255,255,0.65); font-size: 0.9rem; }
.footer-links a:hover { color: var(--secondary-color); padding-left: 5px; }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; margin-top: 40px; text-align: center; }

/* ===== MODAL & FLOATING BUTTONS ===== */
.modal { display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); backdrop-filter: blur(8px); }
.modal-content { background: var(--primary-color); margin: 5% auto; padding: 40px; width: 90%; max-width: 500px; border-radius: 15px; color: #fff; position: relative; border: 1px solid var(--secondary-color); }
.close-modal { position: absolute; right: 20px; top: 15px; font-size: 28px; cursor: pointer; }
.form-group { margin-bottom: 18px; }
.form-group label { display: block; margin-bottom: 6px; font-size: 0.85rem; color: var(--secondary-color); }
.form-group input { width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-radius: 6px; color: #fff; }
.form-row { display: flex; gap: 15px; }

.float-call, .float-whatsapp { position: fixed; bottom: 35px; z-index: 1500; display: flex; align-items: center; gap: 10px; }
.float-call { left: 20px; }
.float-whatsapp { right: 20px; }
.float-btn { width: 54px; height: 54px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; color: white; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: var(--transition); animation: pulse-float 2s infinite; }
.float-btn-call { background: #fff !important; color: #1a73e8 !important; border: 2px solid #1a73e8; }
.float-btn-call i { color: #1a73e8; }
.float-btn-whatsapp { background: #25d366; }
.float-btn:hover { transform: scale(1.1) translateY(-5px); animation: none; }
.float-label { background: #fff; color: #333; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
@keyframes pulse-float { 0%, 100% { box-shadow: 0 4px 15px rgba(0,0,0,0.3); } 50% { box-shadow: 0 4px 25px rgba(0,0,0,0.45); transform: scale(1.05); } }

/* ===== MEDIA QUERIES ===== */
@media (max-width: 992px) {
    .header, .navbar { background: var(--primary-color) !important; padding: 12px 0; }
    .nav-links { display: none; flex-direction: column; position: absolute; top: 100%; left: 0; width: 100%; background: var(--primary-color); padding: 25px; border-top: 1px solid rgba(255,255,255,0.1); }
    .nav-links.active { display: flex; }
    .mobile-menu-icon { display: block; }
    .hero-title { font-size: 3rem; }
    .about-row { flex-direction: column; }
}

@media (max-width: 768px) {
    :root { --section-padding: 60px 20px; }
    .hero { min-height: 100svh; padding-bottom: 50px; align-items: flex-end; }
    .hero-title { font-size: 2.4rem !important; }
    .hero-description { font-size: 0.95rem; margin-bottom: 25px; }
    .booking-search { flex-direction: column; padding: 20px; gap: 15px; width: calc(100% - 30px); margin: 0 15px; }
    .search-divider { display: none; }
    .search-item { width: 100%; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; }
    .search-item:last-of-type { border: none; }
    .search-item:has(.guest-counter) { align-items: center; text-align: center; }
    .guest-counter { margin: 0 auto; }
    .search-btn { width: 100%; justify-content: center; }
    .rooms-grid { grid-template-columns: 1fr; }
    .gallery-grid { grid-template-columns: 1fr 1fr; grid-template-rows: auto; }
    .gallery-item.large { grid-row: span 1; }
    .services-grid { grid-template-columns: 1fr 1fr; }
    .footer-grid { grid-template-columns: 1fr; }
    .modal-content { margin: 15% auto; padding: 25px; }
}

@media (max-width: 480px) {
    .float-label { display: none; }
    .hero-title { font-size: 2rem !important; }
    .services-grid { grid-template-columns: 1fr; }
}

@media (max-width: 380px) {
    .hero-title { font-size: 1.8rem !important; }
}

/* Global Inversion for Phone Icons */
.fa-phone, .fa-phone-alt {
    display: inline-block;
    transform: scaleX(-1);
}
"""

with open(css_file, 'w') as f:
    f.write(clean_css)
