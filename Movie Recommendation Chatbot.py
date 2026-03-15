<!DOCTYPE html>
<!-- saved from url=(0073)https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk- -->
<html lang="en" theme="light" editor="Default Light"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="lohikanneganti05@gmail.com"><script type="text/javascript" async="" charset="utf-8" src="./Movie Recommendation Chatbot_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-obDEicORg1BccYuEfFig6FFh0s3Ho2B7lr6lAHLJGwZTVRSgTgfEKmrfdJ2g/NkT" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./Movie Recommendation Chatbot_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-obDEicORg1BccYuEfFig6FFh0s3Ho2B7lr6lAHLJGwZTVRSgTgfEKmrfdJ2g/NkT" nonce=""></script><script src="./Movie Recommendation Chatbot_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./Movie Recommendation Chatbot_files/cb=gapi.loaded_0" nonce="" async=""></script><script type="text/javascript" async="" src="./Movie Recommendation Chatbot_files/js" nonce=""></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Movie Recommendation Chatbot.ipynb - Colab</title><link href="./Movie Recommendation Chatbot_files/css2" rel="stylesheet"><link href="./Movie Recommendation Chatbot_files/css" rel="stylesheet"><script nonce="">
      window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
    </script><script async="" src="./Movie Recommendation Chatbot_files/analytics.js.download" nonce=""></script><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_yb{font:13px/27px Roboto,Arial,sans-serif;z-index:986}.gb_R{display:none}.gb_Q{background-size:32px 32px;border:0;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_kb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_kb.gb_Q{height:30px;width:30px}.gb_kb.gb_Q:hover,.gb_kb.gb_Q:active{box-shadow:none}.gb_lb{background:#fff;border:none;border-radius:50%;bottom:2px;box-shadow:0px 1px 2px 0px rgba(60,64,67,0.3),0px 1px 3px 1px rgba(60,64,67,0.15);height:14px;margin:2px;position:absolute;right:0;width:14px;line-height:normal;z-index:1}.gb_mb{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25),(min-resolution:1.25dppx){.gb_Q::before,.gb_nb::before{display:inline-block;-webkit-transform:scale(.5);transform:scale(.5);-webkit-transform-origin:left 0;transform-origin:left 0}.gb_4 .gb_nb::before{-webkit-transform:scale(scale(.416666667));transform:scale(scale(.416666667))}}.gb_Q:hover,.gb_Q:focus{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Q:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_Q:active::after{background:rgba(0,0,0,.1);border-radius:50%;content:"";display:block;height:100%}.gb_ob{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_ob{width:auto}.gb_ob:hover,.gb_ob:focus{opacity:.85}.gb_pb .gb_ob,.gb_pb .gb_qb{line-height:26px}#gb#gb.gb_pb a.gb_ob,.gb_pb .gb_qb{font-size:11px;height:auto}.gb_rb{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_0a:hover .gb_rb{opacity:.85}.gb_Xa>.gb_z{padding:3px 3px 3px 4px}.gb_sb.gb_jb{color:#fff}.gb_2 .gb_ob,.gb_2 .gb_rb{opacity:1}#gb#gb.gb_2.gb_2 a.gb_ob,#gb#gb .gb_2.gb_2 a.gb_ob{color:#fff}.gb_2.gb_2 .gb_rb{border-top-color:#fff;opacity:1}.gb_la .gb_Q:hover,.gb_2 .gb_Q:hover,.gb_la .gb_Q:focus,.gb_2 .gb_Q:focus{box-shadow:0 1px 0 rgba(0,0,0,0.15),0 1px 2px rgba(0,0,0,0.2)}.gb_tb .gb_z,.gb_ub .gb_z{position:absolute;right:1px}.gb_z.gb_1,.gb_vb.gb_1,.gb_0a.gb_1{-webkit-box-flex:0;-webkit-flex:0 1 auto;flex:0 1 auto}.gb_wb.gb_xb .gb_ob{width:30px!important}.gb_P{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_yb .gb_P,.gb_zb .gb_P{right:0;top:0}.gb_Ha a.gb_Va{border-radius:100px;background:#0b57d0;background:var(--gm3-sys-color-primary,#0b57d0);box-sizing:border-box;color:#fff;color:var(--gm3-sys-color-on-primary,#fff);display:inline-block;font-size:14px;font-weight:500;min-height:40px;outline:none;padding:10px 24px;text-align:center;text-decoration:none;white-space:normal;line-height:18px;position:relative}.gb_Ha a.gb_Wa{border-radius:100px;border:1px solid;border-color:#747775;border-color:var(--gm3-sys-color-outline,#747775);background:none;box-sizing:border-box;color:#0b57d0;color:var(--gm3-sys-color-primary,#0b57d0);display:inline-block;font-size:14px;font-weight:500;min-height:40px;outline:none;padding:10px 24px;text-align:center;text-decoration:none;white-space:normal;line-height:18px;position:relative}.gb_1a.gb_H a.gb_Va,.gb_2a.gb_H a.gb_Va,.gb_3a.gb_H a.gb_Va{background:#c2e7ff;background:var(--gm3-sys-color-secondary-fixed,#c2e7ff);color:#001d35;color:var(--gm3-sys-color-on-secondary-fixed,#001d35)}.gb_Ha.gb_H a.gb_Wa{color:#a8c7fa;color:var(--gm3-sys-color-primary,#a8c7fa)}.gb_Ha a.gb_Od{padding:10px 12px;margin:12px 16px 12px 10px;min-width:85px}@media (max-width:640px){.gb_Ha a.gb_Od{min-width:75px}}.gb_Ha,.gb_Dd{font-family:"Google Sans Text",Roboto,Helvetica,Arial,sans-serif;font-style:normal}.gb_Ha.gb_1a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a.gb_Pd{background:#fff;background:var(--og-bar-background,var(--gm3-sys-color-background,#fff))}.gb_Ha.gb_1a .gb_pd.gb_qd,.gb_Ha.gb_1a a.gb_Z,.gb_Ha.gb_1a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a .gb_rd .gb_Qd,.gb_Ha.gb_1a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_1a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}@media (forced-colors:active) and (prefers-color-scheme:dark){.gb_Ha svg,.gb_Ha.gb_1a svg,.gb_Ha.gb_H svg{color:white}}.gb_Ha.gb_H.gb_1a{color:#e3e3e3;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a.gb_Pd{background:transparent}.gb_Ha.gb_H.gb_1a .gb_pd.gb_qd,.gb_Ha.gb_H.gb_1a a.gb_Z,.gb_Ha.gb_H.gb_1a span.gb_Z{color:#e3e3e3;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a .gb_rd .gb_Qd,.gb_Ha.gb_H.gb_1a .gb_id .gb_Qd{color:#e3e3e3;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_1a svg{color:#c4c7c5;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#c4c7c5))}.gb_Ha.gb_H.gb_1a.gb_Pd{background:#1f1f1f;background:var(--og-bar-background,var(--gm3-sys-color-background,#131314))}.gb_Ha.gb_2a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a.gb_Pd{background:#e9eef6;background:var(--og-bar-background,var(--gm3-sys-color-surface-container-high,#e9eef6))}.gb_Ha.gb_2a .gb_pd.gb_qd,.gb_Ha.gb_2a a.gb_Z,.gb_Ha.gb_2a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a .gb_rd .gb_Qd,.gb_Ha.gb_2a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_2a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}.gb_Ha.gb_H.gb_2a{color:#e3e3e3;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a.gb_Pd{background:#282a2c;background:var(--og-bar-background,var(--gm3-sys-color-surface-container-high,#282a2c))}.gb_Ha.gb_H.gb_2a .gb_pd.gb_qd,.gb_Ha.gb_H.gb_2a a.gb_Z,.gb_Ha.gb_H.gb_2a span.gb_Z{color:#e3e3e3;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a .gb_rd .gb_Qd,.gb_Ha.gb_H.gb_2a .gb_id .gb_Qd{color:#e3e3e3;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_Ha.gb_H.gb_2a svg{color:#c4c7c5;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#c4c7c5))}.gb_Ha.gb_3a{color:#1f1f1f;color:var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a.gb_Pd{background:transparent}.gb_Ha.gb_3a .gb_pd.gb_qd,.gb_Ha.gb_3a a.gb_Z,.gb_Ha.gb_3a span.gb_Z{color:#1f1f1f;color:var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a .gb_rd .gb_Qd,.gb_Ha.gb_3a .gb_id .gb_Qd{color:#1f1f1f;color:var(--og-logo-color,var(--gm3-sys-color-on-surface,#1f1f1f))}.gb_Ha.gb_3a svg{color:#444746;color:var(--og-svg-color,var(--gm3-sys-color-on-surface-variant,#444746))}.gb_Ha.gb_3a.gb_H.gb_Pd{background:transparent}.gb_Ha.gb_3a.gb_H .gb_pd.gb_qd,.gb_Ha.gb_3a.gb_H a.gb_Z,.gb_Ha.gb_3a.gb_H span.gb_Z{color:white;color:var(--og-theme-color,white)}.gb_Ha.gb_3a.gb_H .gb_rd .gb_Qd,.gb_Ha.gb_3a.gb_H .gb_id .gb_Qd{color:white;color:var(--og-theme-color,white)}.gb_Ha.gb_3a.gb_H svg{color:white;color:var(--og-theme-color,white)}.gb_Ha a.gb_Z,.gb_Ha span.gb_Z{text-decoration:none}.gb_pd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-box-flex:1;-webkit-flex:1 1 auto;flex:1 1 auto}.gb_ud{display:none}.gb_Ha.gb_9a .gb_pd{margin-bottom:0}.gb_rd.gb_sd .gb_pd{padding-left:4px}.gb_Ha.gb_9a .gb_td{position:relative;top:-2px}.gb_Ha{min-width:160px;position:relative}.gb_Ha.gb_ad{min-width:120px}.gb_Ha.gb_Rd .gb_Sd{display:none}.gb_Ha.gb_Rd .gb_Kd{height:56px}header.gb_Ha{display:block}.gb_Ha svg{fill:currentColor}.gb_Td{position:fixed;top:0;width:100%}.gb_Ud{box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Vd{height:64px}.gb_Kd{box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ha:not(.gb_9a) .gb_Kd{padding:8px}.gb_Ha:not(.gb_9a) .gb_Kd a.gb_Wd{margin:12px 8px 12px 10px}.gb_Ha.gb_Xd .gb_Kd{-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ha .gb_Kd.gb_Ld.gb_Zd{min-width:0}.gb_Ha.gb_9a .gb_Kd{padding:4px;padding-left:8px;min-width:0}.gb_Ha.gb_9a .gb_Kd a.gb_Wd{margin:12px 8px 12px 10px}.gb_Sd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none;user-select:none}.gb_0d>.gb_Sd{display:table-cell;width:100%}.gb_rd{padding-right:25px;box-sizing:border-box;-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ha.gb_9a .gb_rd{padding-right:14px}.gb_1d{-webkit-box-flex:1;-webkit-flex:1 1 100%;flex:1 1 100%}.gb_1d>:only-child{display:inline-block}.gb_2d.gb_jd{padding-left:4px}.gb_2d.gb_3d,.gb_Ha.gb_Xd .gb_2d,.gb_Ha.gb_9a:not(.gb_Dd) .gb_2d{padding-left:0}.gb_Ha.gb_9a .gb_2d.gb_3d{padding-right:0}.gb_Ha.gb_9a .gb_2d.gb_3d .gb_Xa{margin-left:10px}.gb_jd{display:inline}.gb_Ha.gb_dd .gb_2d.gb_4d,.gb_Ha.gb_Dd .gb_2d.gb_4d{padding-left:2px}.gb_pd{display:inline-block}.gb_2d{box-sizing:border-box;height:48px;padding:0 4px;padding-left:5px;-webkit-box-flex:0;-webkit-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Dd{height:48px}.gb_Ha.gb_Dd{min-width:auto}.gb_Dd .gb_2d{float:right;padding-left:32px;padding-left:var(--og-bar-parts-side-padding,32px)}.gb_Dd .gb_2d.gb_5d{padding-left:0}.gb_6d{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text;user-select:text}.gb_a a,.gb_6c a{color:inherit}.gb_qd{text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.gb_qd{opacity:1}.gb_7d{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}.gb_0{display:inline-block;padding-left:15px}.gb_0 .gb_Z{display:inline-block;line-height:24px;vertical-align:middle}.gb_8d{text-align:left}.gb_K{display:none}@media screen and (max-width:319px){.gb_Kd .gb_J{display:none;visibility:hidden}}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}.gb_S{display:none!important}.gb_jb{visibility:hidden}@media screen and (max-width:319px){.gb_Kd:not(.gb_Ld) .gb_J{display:none;visibility:hidden}}.gb_vd{display:inline-block;vertical-align:middle}.gb_wd .gb_R{bottom:-3px;right:-5px}@if (RTL_LANG){.gb_wd .gb_R{left:-5px}}.gb_vd:first-child{padding-left:0}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:50%;box-sizing:border-box;height:40px;width:40px}.gb_B,#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}x:-o-prefocus{border-bottom-color:#ccc}.gb_ma{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:0;top:54px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text;user-select:text}.gb_vd.gb_5a .gb_ma,.gb_5a.gb_ma{display:block}.gb_Ad{position:absolute;right:0;top:54px;z-index:-1}.gb_pb .gb_ma{margin-top:-10px}.gb_vd:first-child{padding-left:4px}.gb_Ha.gb_Bd .gb_vd:first-child{padding-left:0}.gb_Cd{position:relative}.gb_id .gb_Cd,.gb_Dd .gb_Cd{float:right}.gb_B{padding:8px;cursor:pointer}.gb_Fd button svg,.gb_B{border-radius:50%}.gb_vd{padding:4px}.gb_Ha.gb_Bd .gb_vd{padding:4px 2px}.gb_Ha.gb_Bd .gb_z.gb_vd{padding-left:6px}.gb_ma{z-index:991;line-height:normal}.gb_ma.gb_Id{left:0;right:auto}@media (max-width:350px){.gb_ma.gb_Id{left:0}}.gb_Jd .gb_ma{top:56px}.gb_z .gb_B{padding:4px}.gb_T{display:none}.gb_0a:not(.gb_Wd){position:relative}.gb_be::after{content:"";border:1px solid #202124;opacity:.13;position:absolute;top:4px;left:4px;border-radius:50%;width:30px;height:30px;box-sizing:content-box}.gb_Xa{box-sizing:border-box;cursor:pointer;display:inline-block;height:48px;overflow:hidden;outline:none;padding:7px 0 0 16px;vertical-align:middle;width:142px;border-radius:28px;background-color:transparent;border:1px solid;position:relative}.gb_Xa .gb_0a{width:32px;height:32px;padding:0}.gb_Xa .gb_R{bottom:-2px;right:-4px}.gb_1a .gb_Xa,.gb_2a .gb_Xa{border-color:#747775;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#747775))}.gb_1a.gb_H .gb_Xa,.gb_2a.gb_H .gb_Xa{border-color:#8e918f;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#8e918f))}.gb_3a .gb_Xa{border-color:#747775;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-outline,#747775))}.gb_3a.gb_H .gb_Xa{border-color:#e3e3e3;border-color:var(--og-dasher-chip-outline,var(--gm3-sys-color-on-surface,#e3e3e3))}.gb_4a{display:inherit}.gb_Xa .gb_4a{background:#fff;border-radius:6px;display:inline-block;left:15px;position:static;padding:2px;top:-1px;height:32px;box-sizing:border-box;width:78px}.gb_6a{text-align:center}.gb_6a.gb_7a{background-color:#f1f3f4}.gb_6a .gb_8a{vertical-align:middle;max-height:28px;max-width:74px}.gb_Ha .gb_Xa .gb_z.gb_vd{padding:0;margin-right:9px;float:right}.gb_Ha:not(.gb_9a) .gb_Xa{margin-left:10px;margin-right:4px}.gb_Xa .gb_be::after{left:0;top:0}@media screen and (max-width:480px){.gb_Xa .gb_4a{display:none}.gb_Xa{border:none;border-radius:50%;height:40px;margin:4px;outline:1px solid transparent;padding:0;width:40px}.gb_Ha .gb_Xa .gb_z.gb_vd{padding:4px;margin-right:0}}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.Rxl3IPTGIww.2019.O","co.in","en","425",0,[4,2,"","","","880583860","0"],null,"O022ad3nHdeEp84PnIvisA0",null,0,"og.qtm.vjyYcS7rQwo.L.W.O","AA2YrTtqMqpQo-Dw21JZNqLnmAiLN5uZVg","AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","lohikanneganti05@gmail.com","","ADUjzeGOgNZJX8Q9mFmCbpql3dv01dAO-WbJxtXT2LMlz2lXiJSa8QKBvVebfNgNRJ8FywNDd9zMc0LBa9OM-RUIz3WHMJrCqg",0,0,null,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.drdv2eaOuoE.O/d=1/rs=AHpOoo9QpDB4BZxPNyi-IhgNVED-jgfZ-w/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20260209.0_p0","en",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en","880583860.0",8,null,1,0,null,null,null,null,"3700949,105109531,105109534,105140909,105140912,115517798,115517801,116249040,116249043",null,null,null,"O022ad3nHdeEp84PnIvisA0",0,0,0,null,2,5,"nn",197,0,0,null,null,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.Rxl3IPTGIww.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTtqMqpQo-Dw21JZNqLnmAiLN5uZVg"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.vjyYcS7rQwo.L.W.O/m=qcwid,qba,d_b_gm3,d_wi_gm3,d_lo_gm3/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?baea=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",null,1,1,0,0,"Account alert",0],null,1,null,1,1,null,null,null,null,0,0,0,null,0,0,null,null,null,null,null,null,null,null,null,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-\u0026timeStmp=1773555003\u0026secTok=.AG5fkS_K6cqqXSnAEu28JRUvSB6aAr3hag\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,null,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-\u0026ec=GAZAqQM",null,null,0,null,null,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,null,null,0,null,0,0,"8559284470",3,1,0,0],0,null,null,null,1,0,"lohikanneganti05@gmail.com",0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles_gbar_=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Fa,Ga,Za,bb,db,ib,eb,kb,qb,Db,Eb,Fb,Gb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Dk=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Ea=function(a,b){return b===void 0?a.j!==Da&&!!(2&(a.ha[_.v]|0)):!!(2&b)&&a.j!==Da};Fa=function(a){return a};Ga=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ha=function(a){a=Error(a);Ga(a,"warning");return a};_.Ja=function(a,b){if(a!=null){var c;var d=(c=Ia)!=null?c:Ia={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ga(a,"incident"),_.ka(a))}};
_.La=function(a){if(typeof a!=="boolean")throw Error("k`"+_.Ka(a)+"`"+a);return a};_.Ma=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Oa=function(a){if(!(0,_.Na)(a))throw _.Ha("enum");return a|0};_.Pa=function(a){if(typeof a!=="number")throw _.Ha("int32");if(!(0,_.Na)(a))throw _.Ha("int32");return a|0};_.Qa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Ra=function(a){return a==null||typeof a==="string"?a:void 0};
_.Ua=function(a,b,c){if(a!=null&&a[_.Sa]===_.Ta)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Xa=function(a){const b=_.Va(_.Wa);return b?a[b]:void 0};Za=function(a,b){b<100||_.Ja(Ya,1)};
bb=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Va(_.Wa),g;!e&&f&&(g=a[f])&&g.Ad(Za);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=$a)!=null?r:Fa)(g-p,p,a,k,void 0)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const E=r-p;var q=void 0;((q=b)!=null?q:b={})[E]=w}else f[r]=w}if(k)for(let w in k){q=
k[w];if(q==null||(q=c(q,d))==null)continue;h=+w;let E;if(m&&!Number.isNaN(h)&&(E=h+p)<g)f[E]=q;else{let O;((O=b)!=null?O:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Va(_.Wa)&&(a=_.Xa(a))&&"function"==typeof _.ab&&a instanceof _.ab&&(f[_.Wa]=a.i());return f};
db=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.cb)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:bb(a,b,db)}if(a!=null&&a[_.Sa]===_.Ta)return eb(a);if("function"==typeof _.fb&&a instanceof _.fb)return a.j();return}return a};ib=function(a,b){if(b){$a=b==null||b===Fa||b[gb]!==hb?Fa:b;try{return eb(a)}finally{$a=void 0}}return eb(a)};
eb=function(a){a=a.ha;return bb(a,a[_.v]|0,db)};
_.lb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error("l");e=a[_.v]|0;if(jb&&1&e)throw Error("m");2048&e&&!(2&e)&&kb();if(e&256)throw Error("n");if(e&64)return(e|d)!==e&&(a[_.v]=e|d),a;if(c&&(e|=128,c!==a[0]))throw Error("o");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("q");for(var h in k)if(f=+h,f<g)c[f+
b]=k[h],delete k[h];else break;e=e&-16760833|(g&1023)<<14;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("r");e=e&-16760833|(h&1023)<<14}}}a[_.v]=e|64|d;return a};kb=function(){if(jb)throw Error("p");_.Ja(mb,5)};
qb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.nb(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Sa]===_.Ta)return b=a.ha,c=b[_.v]|0,_.Ea(a,c)?a:_.ob(a,b,c)?_.pb(a,b):_.nb(b,c);if("function"==typeof _.fb&&a instanceof _.fb)return a};_.pb=function(a,b,c){a=new a.constructor(b);c&&(a.j=Da);a.o=Da;return a};
_.nb=function(a,b,c,d){d!=null||(d=!!(34&b));a=bb(a,b,qb,d);d=32;c&&(d|=2);b=b&16769217|d;a[_.v]=b;return a};_.rb=function(a){const b=a.ha,c=b[_.v]|0;return _.Ea(a,c)?_.ob(a,b,c)?_.pb(a,b,!0):new a.constructor(_.nb(b,c,!1)):a};_.sb=function(a){if(a.j!==Da)return!1;var b=a.ha;b=_.nb(b,b[_.v]|0);b[_.v]|=2048;a.ha=b;a.j=void 0;a.o=void 0;return!0};_.tb=function(a){if(!_.sb(a)&&_.Ea(a,a.ha[_.v]|0))throw Error();};_.ub=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.ob=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.j=Da,!0):!1};_.wb=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>14&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};
_.yb=function(a,b,c,d,e){let f=!1;d=_.xb(a,d,e,g=>{const h=_.Ua(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Ea(d)&&_.ub(a,b),d};_.zb=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(){this.qa=this.qa;this.Y=this.Y};_.Ab=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Bb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Cb=function(a){for(const b in a)return!1;return!0};
Db=Object.defineProperty;Eb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Fb=Eb(this);Gb=function(a,b){if(b)a:{var c=Fb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Db(c,a,{configurable:!0,writable:!0,value:b})}};
Gb("globalThis",function(a){return a||Fb});Gb("Symbol.dispose",function(a){return a?a:Symbol("b")});var Jb,Kb,Nb;_.Hb=_.Hb||{};_.t=this||self;Jb=function(a,b){var c=_.Ib("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Kb=_.t._F_toggles_gbar_||[];_.Ib=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ka=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Lb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Mb="closure_uid_"+(Math.random()*1E9>>>0);
Nb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Nb;return _.z.apply(null,arguments)};_.Ob=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Va=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.vk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Pb=!!(Kb[0]>>19&1),Qb=!!(Kb[0]>>14&1),Rb=!!(Kb[0]>>21&1),Sb=!!(Kb[0]&512),Tb=!!(Kb[0]&64),Ub=!!(Kb[0]&2048);var na,jb;na=Pb?Rb:Jb(610401301,!1);jb=Pb?Qb||!Sb:Jb(748402147,!0);_.Vb=Pb?Qb||!Tb:Jb(824648567,!0);_.Wb=Pb?Qb||!Ub:Jb(824656860,!0);_.Xb=_.ba(a=>a!==null&&a!==void 0);var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var $b,Yb,ac,Zb;_.cb=_.ba(a=>fa?a>=Yb&&a<=Zb:a[0]==="-"?ja(a,$b):ja(a,ac));$b=Number.MIN_SAFE_INTEGER.toString();Yb=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;ac=Number.MAX_SAFE_INTEGER.toString();Zb=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.bc=typeof TextDecoder!=="undefined";_.cc=typeof TextEncoder!=="undefined";var oa,dc=_.t.navigator;oa=dc?dc.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.ec=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.fc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.hc=function(a){_.hc[" "](a);return a};_.hc[" "]=function(){};var uc;_.ic=_.ra();_.jc=_.sa();_.kc=_.u("Edge");_.lc=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.mc=_.ma()&&!_.u("Edge");_.nc=_.za();_.oc=wa()?oa.platform==="Windows":_.u("Windows");_.pc=wa()?oa.platform==="Android":_.u("Android");_.qc=xa();_.rc=_.u("iPad");_.sc=_.u("iPod");_.tc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.lc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.kc)return/Edge\/([\d\.]+)/.exec(c);if(_.jc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.mc)return/WebKit\/(\S+)/.exec(c);if(_.ic)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.jc){var vc;const c=_.t.document;vc=c?c.documentMode:void 0;if(vc!=null&&vc>parseFloat(a)){uc=String(vc);break a}}uc=a}_.wc=uc;_.xc=_.ta();_.yc=xa()||_.u("iPod");_.zc=_.u("iPad");_.Ac=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.Bc=ua();_.Cc=_.va()&&!_.ya();var Ya,mb,gb;_.Wa=_.Ca();_.Dc=_.Ca();Ya=_.Ca();_.Ec=_.Ca();mb=_.Ca();_.Sa=_.Ca("m_m",!0);gb=_.Ca();_.Fc=_.Ca();var Hc;_.v=_.Ca("jas",!0);Hc=[];Hc[_.v]=7;_.Gc=Object.freeze(Hc);var Da;_.Ta={};Da={};_.Ic=Object.freeze({});var hb={};var Ia=void 0;_.Jc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Kc=Number.isSafeInteger;_.Na=Number.isFinite;_.Lc=Math.trunc;var $a;_.Mc=_.ia(0);_.Nc={};_.Oc=function(a,b,c,d,e){b=_.xb(a.ha,b,c,e);if(b!==null||d&&a.o!==Da)return b};_.xb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Pc=function(a,b,c,d){_.tb(a);const e=a.ha;_.wb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.ha,f=e[_.v]|0;b=_.yb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Ea(a,f)){const g=_.rb(b);g!==b&&(_.sb(a)&&(e=a.ha,f=e[_.v]|0),b=g,f=_.wb(e,f,c,b,d),_.ub(e,f))}return b};_.D=function(a,b,c){c==null&&(c=void 0);_.Pc(a,b,c);c&&!_.Ea(c)&&_.ub(a.ha);return a};_.F=function(a,b,c=!1,d){let e;return(e=_.Ma(_.Oc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Ra(_.Oc(a,b,d)))!=null?e:c};_.H=function(a,b,c){return _.Ra(_.Oc(a,b,c,_.Nc))};
_.J=function(a,b,c,d){return _.Pc(a,b,c==null?c:_.La(c),d)};_.K=function(a,b,c){return _.Pc(a,b,c==null?c:_.Pa(c))};_.L=function(a,b,c,d){return _.Pc(a,b,_.Qa(c),d)};_.M=function(a,b,c,d){return _.Pc(a,b,c==null?c:_.Oa(c),d)};_.N=class{constructor(a,b,c){this.ha=_.lb(a,b,c,2048)}toJSON(){return ib(this)}wa(a){return JSON.stringify(ib(this,a))}};_.N.prototype[_.Sa]=_.Ta;_.N.prototype.toString=function(){return this.ha.toString()};_.Qc=_.zb();_.Sc=_.zb();_.Tc=_.zb();_.Uc=Symbol();var Vc=class extends _.N{constructor(a){super(a)}};_.Wc=class extends _.N{constructor(a){super(a)}D(a){return _.K(this,3,a)}};_.Xc=class extends _.N{constructor(a){super(a)}};_.x.prototype.qa=!1;_.x.prototype.isDisposed=function(){return this.qa};_.x.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.x.prototype[Symbol.dispose]=function(){this.dispose()};_.x.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Yc=class extends _.x{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}yb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].yb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var $c=class extends _.x{constructor(){var a=_.Zc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.ad=class extends _.N{constructor(a){super(a)}};var bd=class extends _.N{constructor(a){super(a)}};var ed;_.cd=function(a,b,c=98,d=new _.Wc){if(a.i){const e=new Vc;_.L(e,1,b.message);_.L(e,2,b.stack);_.K(e,3,b.lineNumber);_.M(e,5,1);_.D(d,40,e);a.i.log(c,d)}};ed=class{constructor(){var a=dd;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Wc){_.cd(this,a,98,c)}};var fd,gd;fd=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.ec(c,b,a)}catch(d){console.error(d)}}}};_.hd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new gd(a,b,c));fd(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.i=a;fd(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.j=a;fd(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
gd=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.id=a=>{var b="uc";if(a.uc&&a.hasOwnProperty(b))return a.uc;b=new a;return a.uc=b};_.P=class{constructor(){this.v=new _.hd;this.i=new _.hd;this.D=new _.hd;this.B=new _.hd;this.C=new _.hd;this.A=new _.hd;this.o=new _.hd;this.j=new _.hd;this.F=new _.hd;this.G=new _.hd}K(){return this.v}qa(){return this.i}O(){return this.D}M(){return this.B}P(){return this.C}L(){return this.A}Y(){return this.o}J(){return this.j}N(){return this.F}static i(){return _.id(_.P)}};var ld;_.kd=function(){return _.C(_.jd,_.Xc,5)};ld=class extends _.N{constructor(a){super(a)}};var md;window.gbar_&&window.gbar_.CONFIG?md=window.gbar_.CONFIG[0]||{}:md=[];_.jd=new ld(md);var dd;dd=_.C(_.jd,bd,3)||new bd;_.Zc=new ed;_.A("gbar_._DumpException",function(a){_.Zc?_.Zc.log(a):console.error(a)});_.nd=new $c;var pd;_.qd=function(a,b){var c=_.od.i();if(a in c.i){if(c.i[a]!=b)throw new pd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Cb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.od=class{constructor(){this.i={};this.j={}}static i(){return _.id(_.od)}};_.rd=class extends _.aa{constructor(){super()}};pd=class extends _.rd{};_.A("gbar.A",_.hd);_.hd.prototype.aa=_.hd.prototype.then;_.A("gbar.B",_.P);_.P.prototype.ba=_.P.prototype.qa;_.P.prototype.bb=_.P.prototype.O;_.P.prototype.bd=_.P.prototype.P;_.P.prototype.bf=_.P.prototype.K;_.P.prototype.bg=_.P.prototype.M;_.P.prototype.bh=_.P.prototype.L;_.P.prototype.bj=_.P.prototype.Y;_.P.prototype.bk=_.P.prototype.J;_.P.prototype.bl=_.P.prototype.N;_.A("gbar.a",_.P.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var sd=new Yc;_.qd("api",sd);
var td=_.kd()||new _.Xc,ud=window,vd=_.y(_.H(td,8));ud.__PVT=vd;_.qd("eq",_.nd);
}catch(e){_._DumpException(e)}
try{
_.wd=class extends _.N{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var xd=class extends _.N{constructor(a){super(a)}};var yd=class extends _.x{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.H(a,1));_.Ma(_.Oc(a,12))!=null&&(d.dpo=_.Ab(_.F(a,12)));d.ms=_.y(_.H(a,2));d.m=_.y(_.H(a,3));d.l=[];_.G(b,1)&&(a=_.H(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.H(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var zd=_.C(_.jd,_.ad,14);if(zd){var Ad=_.C(_.jd,_.wd,9)||new _.wd,Bd=new xd,Dd=new yd;Dd.init(zd,Ad,Bd);_.qd("gs",Dd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_lohikanneganti05@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./Movie Recommendation Chatbot_files/bundle.css"><script nonce="">var colabVersionTag = 'colab-external_20260312-060045_RC00_882467244'; var colabScsVersion = 'd06aef58f85b4959b88fff2b48fc3565'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_prompt_cell\x22: true, \x22agent_client_update_task_max_request_size_bytes\x22: 10000000, \x22agent_scroll_delay_ms\x22: 200, \x22agent_update_task_max_request_size_bytes\x22: 10000000, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_service_client_type\x22: \x22\x22, \x22ai_user_input_char_limit\x22: 100000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_subpaths_in_kernel_url\x22: true, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22assign_ping_hostname\x22: \x22https:\/\/ping.prod.colab.dev\x22, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22, \x22*.proxy.googlers.com\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 600000, \x22colab_fetch_try_reauth\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: true, \x22composer_autocomplete\x22: false, \x22composer_client_events_context\x22: true, \x22composer_compaction_interval\x22: 25, \x22composer_compaction_overlap_size\x22: 5, \x22composer_context_max_variable_length\x22: 500000, \x22composer_custom_context\x22: false, \x22composer_default_dock_right\x22: true, \x22composer_early_stopping_for_image_truncation\x22: false, \x22composer_focused_cell_context\x22: true, \x22composer_fp_context\x22: false, \x22composer_generate_code\x22: true, \x22composer_generated_cell_placement_logic\x22: true, \x22composer_kernel_files_in_context\x22: true, \x22composer_model_strategy\x22: 0, \x22composer_replace_empty_cells_when_adding_new_cells\x22: false, \x22composer_show_debug_info\x22: false, \x22composer_show_single_diff_buttons\x22: false, \x22composer_suggestion_chips_in_chat\x22: false, \x22composer_transform_code\x22: true, \x22composer_visible_cells_context\x22: true, \x22connect_enterprise_vm\x22: true, \x22converse_notebook_context_length\x22: 40000, \x22critique_comments\x22: false, \x22data_inspector\x22: true, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecated_accelerator_models\x22: \x5b\x22V28\x22\x5d, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_agent_pending_markdown_network_requests\x22: false, \x22drop_chat_links\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22edu_promotion_banner\x22: false, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_bigquery_data_explorer\x22: false, \x22enable_colab_mcp_integration\x22: true, \x22enable_composer_changeset_plan_stacking\x22: true, \x22enable_composer_code_report\x22: false, \x22enable_composer_fp_orcas_integration\x22: false, \x22enable_composer_fp_orcas_integration_v2\x22: false, \x22enable_composer_g_4_g_models\x22: true, \x22enable_composer_generated_cell_insertion_position\x22: false, \x22enable_composer_suggestion_chips\x22: true, \x22enable_composer_text_cell_transformations\x22: true, \x22enable_dsa_agent_steps_bundle\x22: false, \x22enable_fp_user_provided_context_links\x22: false, \x22enable_g_4_g_as_default_model\x22: true, \x22enable_gcp_preferences\x22: false, \x22enable_gemini_3_flash\x22: true, \x22enable_iframe_unloading\x22: true, \x22enable_improved_composer_context_mentions\x22: false, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_prism_mode\x22: false, \x22enable_rt_on_create\x22: false, \x22enable_vscode_telemetry\x22: true, \x22execution_status_propagation\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22is_prober\x22: false, \x22jspb_analytics\x22: true, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_backend_runtime_selector\x22: false, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: true, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22migrate_assignments\x22: true, \x22migrate_ccu_info\x22: true, \x22migrate_delete_assignment\x22: false, \x22migrate_tfe_keep_alive\x22: true, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22moma_rag_composer\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: false, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22oneplatform_api_key\x22: \x22AIzaSyA2BvntLwNwFthUB4w6_Bhn0cMlVHwyaHc\x22, \x22oneplatform_endpoint\x22: \x22https:\/\/colab.clients6.google.com\x22, \x22optimize_composer_context_order\x22: false, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22pds_minting\x22: false, \x22preference_deep_equality_check\x22: true, \x22prereq_cells_next_steps\x22: true, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduce_composer_planning_overeagerness\x22: true, \x22refresh_warning_timeout_ms\x22: 604800000, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr_skip_fallback\x22: true, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: false, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22runtime_version_names\x22: \x5b\x222026.01\x22, \x222025.10\x22, \x222025.07\x22\x5d, \x22server_execution_queue\x22: true, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_chars_limit\x22: -1, \x22smartpaste_serving_config\x22: \x22freeform_servomatic_goose_v3_xs_smart_paste\x22, \x22snippets_ui_refresh\x22: false, \x22sql_cell\x22: false, \x22sql_completion_lsp\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 4000, \x22task_service_poll_interval_growth_factor\x22: 1.3, \x22task_service_poll_timeout_ms\x22: 300000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_resource_stats\x22: false, \x22transform_code\x22: false, \x22trim_filename_extension\x22: false, \x22truncate_composer_execution_results\x22: true, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_kernel_state_metadata_adk\x22: false, \x22use_kkb_if_configured\x22: false, \x22use_refactored_constraints\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22G4\x22, \x22H100\x22, \x22L4\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22user_visible_composer_tools\x22: \x5b\x5d, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22vscode_test_feature\x22: \x22prod\x22, \x22want_completions_ai_consent_campaign\x22: true, \x22ids\x22: \x5b20730640, 20730652, 20730622, 20730559, 20730660, 20730460, 20730457, 20730183, 20730556, 20730583\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_prompt_cell\x22: 45644995, \x22agent_client_update_task_max_request_size_bytes\x22: 45712580, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_service_client_type\x22: 45723040, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22assign_ping_hostname\x22: 45747049, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22colab_fetch_try_reauth\x22: 45713304, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_autocomplete\x22: 45718105, \x22composer_client_events_context\x22: 45729342, \x22composer_compaction_interval\x22: 45749782, \x22composer_compaction_overlap_size\x22: 45749781, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_custom_context\x22: 45728743, \x22composer_default_dock_right\x22: 45755037, \x22composer_early_stopping_for_image_truncation\x22: 45719141, \x22composer_focused_cell_context\x22: 45697545, \x22composer_fp_context\x22: 45701859, \x22composer_generate_code\x22: 45702500, \x22composer_generated_cell_placement_logic\x22: 45721730, \x22composer_kernel_files_in_context\x22: 45701855, \x22composer_model_strategy\x22: 45711731, \x22composer_replace_empty_cells_when_adding_new_cells\x22: 45788233, \x22composer_show_debug_info\x22: 45700003, \x22composer_show_single_diff_buttons\x22: 45723066, \x22composer_suggestion_chips_in_chat\x22: 45757782, \x22composer_transform_code\x22: 45700458, \x22composer_visible_cells_context\x22: 45716167, \x22connect_enterprise_vm\x22: 45730782, \x22converse_notebook_context_length\x22: 45705427, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecated_accelerator_models\x22: 45724327, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_agent_pending_markdown_network_requests\x22: 45768013, \x22drop_chat_links\x22: 45646864, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22edu_promotion_banner\x22: 45740730, \x22embedded_use_websockets\x22: 45691694, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_bigquery_data_explorer\x22: 45765771, \x22enable_colab_mcp_integration\x22: 45741279, \x22enable_composer_changeset_plan_stacking\x22: 45744296, \x22enable_composer_code_report\x22: 45708595, \x22enable_composer_fp_orcas_integration\x22: 45744285, \x22enable_composer_fp_orcas_integration_v2\x22: 45758361, \x22enable_composer_g_4_g_models\x22: 45745479, \x22enable_composer_generated_cell_insertion_position\x22: 45763491, \x22enable_composer_suggestion_chips\x22: 45710464, \x22enable_composer_text_cell_transformations\x22: 45758370, \x22enable_dsa_agent_steps_bundle\x22: 45755666, \x22enable_fp_user_provided_context_links\x22: 45746774, \x22enable_g_4_g_as_default_model\x22: 45745683, \x22enable_gcp_preferences\x22: 45762481, \x22enable_gemini_3_flash\x22: 45749994, \x22enable_iframe_unloading\x22: 45765934, \x22enable_improved_composer_context_mentions\x22: 45721452, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_prism_mode\x22: 45765531, \x22enable_rt_on_create\x22: 45667583, \x22enable_vscode_telemetry\x22: 45760437, \x22execution_status_propagation\x22: 45644828, \x22explain_error_model_id_override\x22: 45631875, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22is_prober\x22: 45429104, \x22jspb_analytics\x22: 45704358, \x22jsraw\x22: 45425557, \x22kaggle_backend_runtime_selector\x22: 45704319, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22migrate_assignments\x22: 45752830, \x22migrate_ccu_info\x22: 45716751, \x22migrate_delete_assignment\x22: 45760675, \x22migrate_tfe_keep_alive\x22: 45766773, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22moma_rag_composer\x22: 45706746, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22oneplatform_api_key\x22: 45717742, \x22oneplatform_endpoint\x22: 45717924, \x22optimize_composer_context_order\x22: 45759155, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22pds_minting\x22: 45648255, \x22preference_deep_equality_check\x22: 45740961, \x22prereq_cells_next_steps\x22: 45640400, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduce_composer_planning_overeagerness\x22: 45758628, \x22refresh_warning_timeout_ms\x22: 45765093, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22runtime_version_names\x22: 45714997, \x22server_execution_queue\x22: 45425600, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_chars_limit\x22: 45714219, \x22smartpaste_serving_config\x22: 45630585, \x22snippets_ui_refresh\x22: 45737461, \x22sql_cell\x22: 45425497, \x22sql_completion_lsp\x22: 45688254, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_resource_stats\x22: 45655215, \x22transform_code\x22: 45667102, \x22trim_filename_extension\x22: 45691676, \x22truncate_composer_execution_results\x22: 45746694, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_kernel_state_metadata_adk\x22: 45737477, \x22use_kkb_if_configured\x22: 45733350, \x22use_refactored_constraints\x22: 45740233, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_composer_tools\x22: 45752901, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22vscode_test_feature\x22: 45755614, \x22want_completions_ai_consent_campaign\x22: 45671138\x7d\x7d'); var colabUserEmail = 'lohikanneganti05@gmail.com'; var colabRenderDataToken = 'AFWLbD3O-VRJHcv3F7XpsfkxugfGIshF-8hgY2JnPI_Aa7P76V_C7W1DZ47RdosA_TqGzimVMtaXh0n_C7gUbtysXprey5hYBliHZbnxvLrG5Mju'; var colabConfig = '\x5b\x5b\x22lohikanneganti05@gmail.com\x22,\x5b1,\x22AHXL0D0RzM28WFJRsQ3XicrI90KS9F74TOydMBBx45HrEpaGqnwPJ7Nev5GPK5307FDUaBRuTW7XllTUxm3y5kmrdnlWY9JgPULpoLsLf7js590rmB\/UuDLsLkiM5VIwcasF9xzrRff4eASuiNYcuhsxHAzI5wuwWOa6izzXvMKP1Syc31hplyqCVHXTIaSjNCObkH3m3ppvPTR\/VQmATrSdDZpcFkfcbEFTuYl3qWWIVA7yF5QlsIPyYgjYnQlFgumR5jXIDDC1IOYRuKLzyV8hR\/IYUFkfcuJNBD59hcSisP+Pojtn6Ihb\/06jaSrzIeM1fG12pxz6\/J84wDYboPmoMJQyEU6iRaImRbXRQnpe9YXSah9kIliCVufRdv0lRkYdVF5LnL4eUUBOz37Iz7rePfRevZOe1HlNivipB99v\/0FoHUyqa2rz+7ulMmn9NG19pSPtlrLdr0Ncv+zyqAo7crc\/mHen\/NnYVOOBe4dHLiCPfjOC79CKyGg6IqiXYMnInRn4Buicm9tWEDFWDGjNNc4Xvp0a9xbuuYViMkD2S6T6smJc1zsSJ86EHOQ7M5HHXUY\/vwfBMkwjnLYWjjfYyYeZJ+yfDWOkZO\/0R9XKXFfxmIv23cG0aJ4KgiiNzweoN35HxYjTvYpq27DXydA0QTs3LBY2voZUeLtr8wGsQ0bIJEl2HjGRu0Um9WP5O9aruJcsCpnGKMyaJpxhV+TLjBvTMfa7WlQ0k3Zr99DXfW1dMrmC\/1Ezys2a9jDUEbJR4cB2\/ucy4moYFRK4i13dtkezg4q1b5U4OOApG3ncZ\/TDEeRjhWICdIWZh3nF8cwCdH29sT9ZdhA4KVrBGKNcUIZZmc0aItNvxymsP\/R3scYXia+Fyr7yQ9KHe35ONIPovKODjl+P5tDDPNgDsSW+s9AKxFbItmo4G1CyMtpa0s3fqUgOvMVqCsREZTi2\/OMatowgTFnTHlNfRK25FyNFjWUahGXoF8f70xD7x83g\/YEV93TJ8nc1butddIDV\/1hVv0T\/CVo47+Mv3ose7RcCepZ+q2I\/oiOAw1AkD\/jz319dV9028t7S6Qjlqop3xvj9bkj\/NbdhNxuOgbCVGOjW0RD9uGpZJI8UWzmK4TChhe2Ua+fgZt8jGWGHnpRX1TpOtfmEn1y8A0B5YbLEK3DB1aPO5J86dsor3ixuVGCQejIyPgO+iO5Cwe2Is+JocobGozSSEAYuAb5R+fD3npaenIl7Dc+v5k4u5B\/LRRXu2WKcK2BdwTqjEpVCnAwHkgzwSkdFkmvPpYv17WneScQWOoCL7ppjVYoli7HgYtWRVv5W0nzCtzYneSQ8A9TWOqwwwhRNFro5pWvLBPH5k5oH3cSB\/6yoy9CG6TNDqSw9UCvDPzsD\/qFIza1Rf\/mYb5hfaaJd27APH1RvkOCcMzTsrFOdq1V8wpwz1mi4VWEYIcH4Rs6exWTknmbCa49AZtwWKxE13P\/3TbqEdqL47kyM\/9bPnRmmKR897ah\/TTWEOKrDcUQxft0NQRIY8eOChCKUFdpdcPMGRcj66p\/Mqf49K2v4pHmB1yCJfv82JbVi9dVUuIlGO\/\/dXhz7rjXOR5h3mFtAlrQtuxKTYCOFH61WPdGgtrct40bFcaIy45X3\/VKcPx1c65SXezXVip2CbLxpOsmRvrCke+KSpEC6qtxeG1RljsmSc0W8k\/5yIIqQu7n9EoKiWS2mZ6SfDTjnjIYWJMoovzGEbfRTYG5pBxkk9J7oW114iNwEpyjul0vsO\/sQRO5dTqOEL3ONVNEze0asPE0BlgaMsTEzLWkFhtwPk6QnX1ta4qr7Z9Vq4giDHAb\/m\/BYnhFC0okcCbDFY+0MP6ju4Uva+e3j8ExcRCe71gXEyhgGNM3VGuEade7818eh\/sjOMa+H5qO0ITgSNOvbaceRwEEfxfZjUVmmubvzM6dXkvK1cq7e08tNCkEc8lXzXGuEuvAN9GiVgeyZuA33YCAu15Hx\x22,\x22AJ9oCCw8o17YrejT0lf2r3nyaRcWv9zwktUp4jgffoksU7Y7U+70eG427WorXbbFBCP9lvKfgp7ck+CJjPLwB14omDoYZ2qOfn9mx0YUT\/\/HwSMJyVMXtQrN7PLc1d0U5N56VbpKl+oF\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22,0,0,0\x5d,\x5b1,4,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/d06aef58f85b4959b88fff2b48fc3565/img/favicon.ico"><meta name="google-site-verification" content="h4AyILcMXlXf3PDJKg3Fu2_dyS3jfH5im5G__oDgjOs"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="gl3hNNVi7GnXImkDiRAkUxkhUD4g7Ke8L4D6Ve8FEVY"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="HwWGKCyRK7kxGyAlA30sbbTly9VW0SOM7Sh4juqiOVA"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./Movie Recommendation Chatbot_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="async" type="text/javascript" src="./Movie Recommendation Chatbot_files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./Movie Recommendation Chatbot_files/rs=AA2YrTtqMqpQo-Dw21JZNqLnmAiLN5uZVg" nonce=""></script><link type="text/css" href="./Movie Recommendation Chatbot_files/rs=AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww" rel="stylesheet"><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./Movie Recommendation Chatbot_files/editor.main.css"><script async="async" type="text/javascript" src="./Movie Recommendation Chatbot_files/editor.main.nls.js.download"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script src="./Movie Recommendation Chatbot_files/api.js.download" nonce=""></script><script src="./Movie Recommendation Chatbot_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #ffffff; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor { --vscode-foreground: #616161;
--vscode-disabledForeground: rgba(97, 97, 97, 0.5);
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textPreformat-foreground: #a31515;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-foreground: #616161;
--vscode-dropdown-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-sash-hoverBorder: #0090f1;
--vscode-editor-background: #ffffff;
--vscode-editor-foreground: #000000;
--vscode-editorStickyScroll-background: #ffffff;
--vscode-editorStickyScrollHover-background: #f0f0f0;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: #616161;
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editorInlayHint-foreground: #616161;
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-typeForeground: #616161;
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-parameterForeground: #616161;
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.3);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-diffEditor-insertedTextBackground: #aceebb;
--vscode-diffEditor-removedTextBackground: #ffcecb;
--vscode-diffEditor-insertedLineBackground: #dafbe1;
--vscode-diffEditor-removedLineBackground: #ffebe9;
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #e4e4e4;
--vscode-diffEditor-unchangedRegionForeground: #4d4c4c;
--vscode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #d6ebff;
--vscode-list-activeSelectionForeground: #000000;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #0066bf;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #f3f3f3;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.16);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-inactiveIndentGuidesStroke: rgba(169, 169, 169, 0.4);
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-selectBackground: #f3f3f3;
--vscode-checkbox-foreground: #616161;
--vscode-checkbox-border: #cecece;
--vscode-checkbox-selectBorder: #424242;
--vscode-quickInputList-focusForeground: #000000;
--vscode-quickInputList-focusBackground: #d6ebff;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #000000;
--vscode-menu-selectionBackground: #d6ebff;
--vscode-menu-separatorBackground: #d4d4d4;
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #ffffff;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(0, 0, 0, 0);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background: #d3d3d3;
--vscode-editorIndentGuide-activeBackground: #939393;
--vscode-editorLineNumber-foreground: #999999;
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #ffffff;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #cea33d;
--vscode-editorUnicodeHighlight-background: rgba(206, 163, 61, 0.08);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: #d6ebff;
--vscode-editor-wordHighlightTextBackground: rgba(173, 214, 255, 0.45);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(0, 0, 0, 0);
--vscode-peekViewTitle-background: #f3f3f3;
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewEditorStickyScroll-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #ffffff;
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #000000;
--vscode-editorSuggestWidget-selectedBackground: #d6ebff;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #0066bf;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editorGutter-foldingControlForeground: #424242; }

.mtk1 { color: #000000; }
.mtk2 { color: #ffffff; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #811f3f; }
.mtk11 { color: #a53434; }
.mtk12 { color: #116644; }
.mtk13 { color: #383838; }
.mtk14 { color: #257693; }
.mtk15 { color: #6a5221; }
.mtk16 { color: #001080; }
.mtk17 { color: #cd3131; }
.mtk18 { color: #863b00; }
.mtk19 { color: #9723b4; }
.mtk20 { color: #af00db; }
.mtk21 { color: #a31515; }
.mtk22 { color: #800000; }
.mtk23 { color: #e00000; }
.mtk24 { color: #3030c0; }
.mtk25 { color: #666666; }
.mtk26 { color: #778899; }
.mtk27 { color: #c700c7; }
.mtk28 { color: #4f76ac; }
.mtk29 { color: #008080; }
.mtk30 { color: #001188; }
.mtk31 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="" style=""><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./Movie Recommendation Chatbot_files/gapi_loader.js.download" nonce=""></script><script src="./Movie Recommendation Chatbot_files/socketio_binary.js.download" nonce=""></script><script src="./Movie Recommendation Chatbot_files/MathJax.js.download" nonce=""></script><script src="./Movie Recommendation Chatbot_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./Movie Recommendation Chatbot_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$453401876$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$453401876$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    <md-text-button class="snackbar-action" slot="action" value="" trailing-icon="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$453401876$--><a id="link" class="button" href="https://github.com/Lohitha-19/Movie-Recommendation-Chatbot/blob/main/Movie_Recommendation_Chatbot.ipynb" target="_blank"><!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$-->
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
    
    </a>
    </template><!--?lit$453401876$-->Re-open<!----><md-icon slot="icon" role="img" aria-label="Link will open in a new tab"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon></md-text-button></colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$453401876$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$453401876$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_T" ng-non-bindable=""><div class="gb_Rc"><div>Google Account</div><div class="gb_g">Kanneganti Lohitha</div><div>lohikanneganti05@gmail.com</div><div class="gb_Sc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Nd;Nd=class extends _.rd{};_.Od=function(a,b){if(b in a.i)return a.i[b];throw new Nd;};_.Pd=function(a){return _.Od(_.od.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Sd;_.Qd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Sd=function(a){return new _.Rd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Td=globalThis.trustedTypes;_.Ud=class{constructor(a){this.i=a}toString(){return this.i}};_.Vd=new _.Ud("about:invalid#zClosurez");_.Rd=class{constructor(a){this.Vh=a}};_.Wd=[Sd("data"),Sd("http"),Sd("https"),Sd("mailto"),Sd("ftp"),new _.Rd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Xd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Yd=new _.Xd(_.Td?_.Td.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var ce,oe,re,be,de,ie;_.Zd=function(a){return a==null?a:(0,_.Na)(a)?a|0:void 0};_.$d=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Na)(a)?a|0:void 0};_.ae=function(a,b){return a.lastIndexOf(b,0)==0};ce=function(){let a=null;if(!be)return a;try{const b=c=>c;a=be.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.ee=function(){de===void 0&&(de=ce());return de};
_.ge=function(a){const b=_.ee();a=b?b.createScriptURL(a):a;return new _.fe(a)};_.he=function(a){if(a instanceof _.fe)return a.i;throw Error("x");};_.je=function(a){if(ie.test(a))return a};_.ke=function(a){if(a instanceof _.Ud)if(a instanceof _.Ud)a=a.i;else throw Error("x");else a=_.je(a);return a};_.le=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};
_.me=function(a,b,c,d){return _.Zd(_.Oc(a,b,c,d))};_.Q=function(a,b,c){return _.Ma(_.Oc(a,b,c,_.Nc))};_.ne=function(a,b){return _.$d(_.Oc(a,b,void 0,_.Nc))};oe=class extends _.N{constructor(a){super(a)}Yb(a){return _.L(this,24,a)}};_.pe=function(){return _.C(_.jd,oe,1)};_.qe=function(a){var b=_.Ka(a);return b=="array"||b=="object"&&typeof a.length=="number"};be=_.Td;_.fe=class{constructor(a){this.i=a}toString(){return this.i+""}};ie=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var xe,Be,se;_.ue=function(a){return a?new se(_.te(a)):re||(re=new se)};_.ve=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.S=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a=a?(b||c).querySelector(a?"."+a:""):_.we(c,"*",a,b)[0]||null);return a||null};_.we=function(a,b,c,d){a=d||a;return(b=b&&b!="*"?String(b).toUpperCase():"")||c?a.querySelectorAll(b+(c?"."+c:"")):a.getElementsByTagName("*")};
_.ye=function(a,b){_.Bb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:xe.hasOwnProperty(d)?a.setAttribute(xe[d],c):_.ae(d,"aria-")||_.ae(d,"data-")?a.setAttribute(d,c):a[d]=c})};xe={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.ze=function(a){return a?a.defaultView:window};_.Ce=function(a,b){const c=b[1],d=_.Ae(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.ye(d,c));b.length>2&&Be(a,d,b);return d};Be=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.qe(f)||_.Lb(f)&&f.nodeType>0?d(f):_.ec(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Qd(f):f,d)}};
_.De=function(a){return _.Ae(document,a)};_.Ae=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.Ee=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.Fe=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.Ge=function(a,b){return a&&b?a==b||a.contains(b):!1};_.te=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};se=function(a){this.i=a||_.t.document||document};_.n=se.prototype;
_.n.H=function(a){return _.ve(this.i,a)};_.n.Ra=function(a,b,c){return _.Ce(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.Pe=_.Ee;_.n.tg=_.Fe;_.n.rg=_.Ge;
}catch(e){_._DumpException(e)}
try{
_.Qi=function(a){const b=_.le("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Ri=function(a){if(!a)return null;a=_.H(a,4);var b;a===null||a===void 0?b=null:b=_.ge(a);return b};_.Ti=function(a,b,c){a=a.ha;return _.yb(a,a[_.v]|0,b,c)!==void 0};_.Ui=class extends _.N{constructor(a){super(a)}};_.Vi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Xi=function(a,b,c){a<b?Wi(a+1,b):_.Zc.log(Error("W`"+a+"`"+b),{url:c})},Wi=function(a,b){if(Yi){const c=_.De("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.he(Yi);_.Qi(c);c.onerror=_.Ob(Xi,a,b,c.src);_.Vi("HEAD")[0].appendChild(c)}},Zi=class extends _.N{constructor(a){super(a)}};var $i=_.C(_.jd,Zi,17)||new Zi,aj,Yi=(aj=_.C($i,_.Ui,1))?_.Ri(aj):null,bj,cj=(bj=_.C($i,_.Ui,2))?_.Ri(bj):null,dj=function(){Wi(1,2);if(cj){const a=_.De("LINK");a.setAttribute("type","text/css");a.href=_.he(cj).toString();a.rel="stylesheet";let b=_.le("style",document);b&&a.setAttribute("nonce",b);_.Vi("HEAD")[0].appendChild(a)}};(function(){const a=_.pe();if(_.Q(a,18))dj();else{const b=_.ne(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(dj,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./Movie Recommendation Chatbot_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <!--?lit$453401876$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><a id="link" class="button" href="https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-#notebook-main"><!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </a>
    </template><!--?lit$453401876$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$453401876$-->
    <!--?lit$453401876$-->
          <div id="private-outputs-warning" hidden="" class="header-warning private-outputs-warning"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$453401876$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$453401876$--> <!--?lit$453401876$-->
    <div hidden="" class="header-warning refresh-warning undismissible"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
      <div class="message"><!--?lit$453401876$-->Your Colab version is out of date, please refresh to get the latest updates.</div>
      <div class="actions">
        <md-text-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
          <!--?lit$453401876$-->Refresh to update
        </md-text-button>
      </div>
    </div>
  
    <!--?lit$453401876$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><div id="header-logo">
              <!--?lit$453401876$--><!--?lit$453401876$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$453401876$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$--><svg viewBox="0 0 24 24"><!--?lit$453401876$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$453401876$--><!--?lit$453401876$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 335.225px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Movie Recommendation Chatbot.ipynbS_</colab-input-sizer>
            <!--?lit$453401876$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$453401876$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-text-button id="button" class=" save-message " value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->sync</md-icon><!--?lit$453401876$-->Saving...</md-text-button><!--?lit$453401876$--><!--?--></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" style="user-select: none;" tabindex="0"><!--?lit$453401876$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$453401876$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$453401876$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$453401876$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$453401876$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$453401876$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$453401876$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$453401876$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$453401876$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$453401876$-->
      <!--?lit$453401876$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$453401876$--><md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$453401876$--><md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$453401876$--><md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button" aria-label="Share notebook">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->people</md-icon>
                <!--?lit$453401876$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-tooltip" hidden="" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button" aria-label="Toggle Gemini">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
            <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
            <!--?lit$453401876$-->Gemini
          </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Ha gb_Dd gb_yb gb_e gb_3a gb_dd" id="gb"><div class="gb_2d gb_wb gb_Sd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Cd" style="display:block"><div class="gb_jd"></div><div class="gb_z gb_vd gb_Qf gb_1"><div class="gb_D gb_vb gb_Qf gb_1"><a class="gb_B gb_0a gb_1" aria-expanded="false" aria-label="Google Account: Kanneganti Lohitha  
(lohikanneganti05@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/drive/1qX2Cfstx75aON7L745aRaUW0JO0a8Yk-&amp;ec=GBRAqQM" tabindex="0" role="button"><span class="gb_be"><img class="gb_Q gbii" src="./Movie Recommendation Chatbot_files/unnamed.png" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyjF9FvJ0ErLG-gA8-cTWRUFnzunshsRwMgbkCuBW7ovNQ=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyjF9FvJ0ErLG-gA8-cTWRUFnzunshsRwMgbkCuBW7ovNQ=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></span><div class="gb_R gb_S" aria-hidden="true"><svg class="gb_La" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_Ma" cx="7" cy="7" r="7"></circle><path class="gb_Oa" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.Ed=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.Ed(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("t`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Fd=document.querySelector(".gb_J .gb_B"),Gd=document.querySelector("#gb.gb_ad");Fd&&!Gd&&_.Ed(_.nd,Fd,"click");
}catch(e){_._DumpException(e)}
try{
_.rh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ka()&&a.i[b].B())return a.i[b];return null};_.sh=function(a,b){a.i[b.J()]=b};var th=new class extends _.x{constructor(){var a=_.Zc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.rh(this)&&_.rh(this).J()==a||this.i[a].P(!0))}Ua(a){this.j=a;for(const b in this.i)this.i[b].ka()&&this.i[b].Ua(a)}oc(a){return a in this.i?this.i[a]:null}};_.qd("dd",th);
}catch(e){_._DumpException(e)}
try{
_.Ki=function(a,b){return _.J(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Li=document.querySelector(".gb_z .gb_B"),Mi=document.querySelector("#gb.gb_ad");Li&&!Mi&&_.Ed(_.nd,Li,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$453401876$-->
    <!--?lit$453401876$--><colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
        <!--?lit$453401876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$453401876$--><span class="screenreader-only"><!--?lit$453401876$-->Show command palette <!--?lit$453401876$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$453401876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
          <!--?lit$453401876$-->Commands
        </colab-toolbar-button>
    <!--?lit$453401876$--><span class="toolbar-add-code-split"><colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code" class=" split-button "><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
        <!--?lit$453401876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$453401876$--><span class="screenreader-only"><!--?lit$453401876$-->Insert code cell below <!--?lit$453401876$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$453401876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
              <!--?lit$453401876$-->Code
            </colab-toolbar-button>
            <!--?lit$453401876$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" id="top-toolbar-add-code-dropdown-button" data-aria-label="Insert code cell options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert code cell options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="top-toolbar-add-code-dropdown-button" message="Insert code cell options"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Insert code cell options</div><!----><!--?--></template>
    </colab-tooltip-trigger></span>
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
        <!--?lit$453401876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$453401876$--><span class="screenreader-only"><!--?lit$453401876$-->Add text cell <!--?lit$453401876$--></span>
      </md-text-button>
      <!--?lit$453401876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$453401876$-->Text
          </colab-toolbar-button>
    <span class="colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button class="split-button" icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Run all cells in notebook"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
        <!--?lit$453401876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$453401876$--><span class="screenreader-only"><!--?lit$453401876$-->Run all cells in notebook <!--?lit$453401876$--></span>
      </md-text-button>
      <!--?lit$453401876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Run all cells in notebook" shortcut=""><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Run all cells in notebook</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$453401876$-->Run all
      </colab-toolbar-button>
      <!--?lit$453401876$--><md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$453401876$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$453401876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$453401876$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$453401876$--><!----><md-menu-item command="restart" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item  disabled " tabindex="-1"><!--?lit$453401876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$453401876$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$453401876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$453401876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$453401876$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item  disabled " tabindex="-1"><!--?lit$453401876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$453401876$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$453401876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$453401876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$453401876$-->Restart session and run all</span>
  </md-menu-item><!----><!----><md-menu-item command="runafter" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$453401876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$453401876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$453401876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$453401876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$453401876$-->Run focused cell and all cells below</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item  disabled " tabindex="-1"><!--?lit$453401876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$453401876$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$453401876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$453401876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$453401876$-->Interrupt execution</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$453401876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$453401876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$453401876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$453401876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$453401876$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$453401876$-->
    <!--?lit$453401876$-->
    <!--?lit$453401876$-->
    <!--?lit$453401876$-->
    <!--?lit$453401876$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-text-button id="button" class=" save-message " value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->sync</md-icon><!--?lit$453401876$-->Saving...</md-text-button><!--?lit$453401876$--><!--?--></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$453401876$-->
    <!--?lit$453401876$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$453401876$--><!--?--></template></colab-connect-warning-button>
    <!--?lit$453401876$--><!--?lit$453401876$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$453401876$--> <!--?lit$453401876$--><!--?-->
      <colab-toolbar-button id="connect" class="split-button" tooltipid="colab-connect-tooltip" tooltiptext="Connect to a new runtime"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
        <!--?lit$453401876$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$453401876$--><span class="screenreader-only"><!--?lit$453401876$-->Connect to a new runtime <!--?lit$453401876$--></span>
      </md-text-button>
      <!--?lit$453401876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connect to a new runtime" shortcut=""><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Connect to a new runtime</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$453401876$-->Connect
      </colab-toolbar-button>
      <!--?lit$453401876$--> <md-icon-button id="connect-dropdown" class="connect-dropdown" touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$453401876$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$453401876$-->
    <span class="collapsed-options">
      <!--?lit$453401876$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$453401876$-->
      <span class="colab-separator"></span>
    </span>
    <!--?lit$453401876$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" touch-target="none" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$453401876$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$453401876$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$453401876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$453401876$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$453401876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$453401876$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->code</md-icon>
    </md-icon-button> <!--?lit$453401876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$453401876$--><md-icon-button toggle="" command="show-data-inspector" data-aria-label="Data inspector" title="Data inspector" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Data inspector" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->eye_tracking</md-icon>
    </md-icon-button> <!--?lit$453401876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$453401876$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$453401876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$453401876$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->folder</md-icon>
    </md-icon-button> <!--?lit$453401876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$453401876$--><md-icon-button toggle="" command="show-data-explorer" data-aria-label="Data explorer" title="Data explorer" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Data explorer" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->table</md-icon>
    </md-icon-button> <!--?lit$453401876$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$453401876$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$453401876$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-98WGLEjZHcJm" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$453401876$--><div class="indicator"></div>
      </div>
      <!--?lit$453401876$-->
    </div></template>
          <div class="colab-tab-header"> <!--?lit$453401876$--><div class="colab-tab-title">
      <!--?lit$453401876$-->
      <span id="tab-title-98WGLEjZHcJm"><!--?lit$453401876$--><!--?lit$453401876$-->Notebook<!--?--></span>
    </div> <!--?lit$453401876$--> </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"><!----><!--?lit$453401876$--><!--?--></div>
      <!--?lit$453401876$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-0-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$453401876$--><md-icon-button id="tab-pane-0-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-scroller role="main" id="notebook-main" class="notebook-container" aria-label="Notebook" tabindex="-1">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$453401876$-->
              <div class="notebook-content ">
                <!--?lit$453401876$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$453401876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$453401876$-->Text
        </md-outlined-button>
        <!--?lit$453401876$-->
        <!--?lit$453401876$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code notebook-cell code-has-output focused" id="cell-6tzb2-U-Py5S" role="region" aria-label="Cell 0: Code cell: " style="" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$453401876$-->Gemini
    </div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value="" soft-disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" aria-disabled="true">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->arrow_upward</md-icon>
        <!--?lit$453401876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Move cell up</div><!----><!----><div><!--?lit$453401876$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->arrow_downward</md-icon>
        <!--?lit$453401876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Move cell down</div><!----><!----><div><!--?lit$453401876$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$453401876$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-6tzb2-U-Py5S" anchor="ai-menu-anchor-6tzb2-U-Py5S" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$453401876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$453401876$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$453401876$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$453401876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$453401876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$453401876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$453401876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$453401876$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$453401876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$453401876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$453401876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$453401876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$453401876$-->Explain code</span>
  </md-menu-item><!----><!----><md-menu-item command="transform-code" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" role="menuitem" class="list-item   " tabindex="0"><!--?lit$453401876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$453401876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$453401876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$453401876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$453401876$-->Transform code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-6tzb2-U-Py5S-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-6tzb2-U-Py5S" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template> pen_spark </md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-6tzb2-U-Py5S" id="ai-menu-anchor-6tzb2-U-Py5S-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->edit</md-icon>
        <!--?lit$453401876$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->delete</md-icon>
        <!--?lit$453401876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Delete cell</div><!----><!----><div><!--?lit$453401876$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$453401876$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$453401876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$453401876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$453401876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Kanneganti Lohitha
10:18 PM (13 hours ago)
executed in 11.499s"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$453401876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$453401876$-->executed by Kanneganti Lohitha</div><!----><!----><div><!--?lit$453401876$-->10:18 PM (13 hours ago)</div><!----><!----><div><!--?lit$453401876$-->executed in 11.499s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$453401876$--><div class="status">
      <div class="execution-count"><!--?lit$453401876$-->[ ]</div>
      <!--?lit$453401876$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="1" data-mode-id="notebook-python" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/3" style="width: 1338px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 1338px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1332px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1332px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1332px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1332px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk6">!</span><span class="mtk1">pip&nbsp;install&nbsp;scikit-learn&nbsp;joblib&nbsp;ipywidgets</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1318px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1318px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="36" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1338px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1338px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="36" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="36" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 767px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" role="tooltip" tabindex="0"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 883.08px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$453401876$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$453401876$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button focused" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group" tabindex="0"><div><div class="stream output_text"><pre>Requirement already satisfied: scikit-learn in /usr/local/lib/python3.12/dist-packages (1.6.1)
Requirement already satisfied: joblib in /usr/local/lib/python3.12/dist-packages (1.5.3)
Requirement already satisfied: ipywidgets in /usr/local/lib/python3.12/dist-packages (7.7.1)
Requirement already satisfied: numpy&gt;=1.19.5 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (2.0.2)
Requirement already satisfied: scipy&gt;=1.6.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (1.16.3)
Requirement already satisfied: threadpoolctl&gt;=3.1.0 in /usr/local/lib/python3.12/dist-packages (from scikit-learn) (3.6.0)
Requirement already satisfied: ipykernel&gt;=4.5.1 in /usr/local/lib/python3.12/dist-packages (from ipywidgets) (6.17.1)
Requirement already satisfied: ipython-genutils~=0.2.0 in /usr/local/lib/python3.12/dist-packages (from ipywidgets) (0.2.0)
Requirement already satisfied: traitlets&gt;=4.3.1 in /usr/local/lib/python3.12/dist-packages (from ipywidgets) (5.7.1)
Requirement already satisfied: widgetsnbextension~=3.6.0 in /usr/local/lib/python3.12/dist-packages (from ipywidgets) (3.6.10)
Requirement already satisfied: ipython&gt;=4.0.0 in /usr/local/lib/python3.12/dist-packages (from ipywidgets) (7.34.0)
Requirement already satisfied: jupyterlab-widgets&gt;=1.0.0 in /usr/local/lib/python3.12/dist-packages (from ipywidgets) (3.0.16)
Requirement already satisfied: debugpy&gt;=1.0 in /usr/local/lib/python3.12/dist-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets) (1.8.15)
Requirement already satisfied: jupyter-client&gt;=6.1.12 in /usr/local/lib/python3.12/dist-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets) (7.4.9)
Requirement already satisfied: matplotlib-inline&gt;=0.1 in /usr/local/lib/python3.12/dist-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets) (0.2.1)
Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.12/dist-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets) (1.6.0)
Requirement already satisfied: packaging in /usr/local/lib/python3.12/dist-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets) (26.0)
Requirement already satisfied: psutil in /usr/local/lib/python3.12/dist-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets) (5.9.5)
Requirement already satisfied: pyzmq&gt;=17 in /usr/local/lib/python3.12/dist-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets) (26.2.1)
Requirement already satisfied: tornado&gt;=6.1 in /usr/local/lib/python3.12/dist-packages (from ipykernel&gt;=4.5.1-&gt;ipywidgets) (6.5.1)
Requirement already satisfied: setuptools&gt;=18.5 in /usr/local/lib/python3.12/dist-packages (from ipython&gt;=4.0.0-&gt;ipywidgets) (75.2.0)
Collecting jedi&gt;=0.16 (from ipython&gt;=4.0.0-&gt;ipywidgets)
  Downloading jedi-0.19.2-py2.py3-none-any.whl.metadata (22 kB)
Requirement already satisfied: decorator in /usr/local/lib/python3.12/dist-packages (from ipython&gt;=4.0.0-&gt;ipywidgets) (4.4.2)
Requirement already satisfied: pickleshare in /usr/local/lib/python3.12/dist-packages (from ipython&gt;=4.0.0-&gt;ipywidgets) (0.7.5)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0 in /usr/local/lib/python3.12/dist-packages (from ipython&gt;=4.0.0-&gt;ipywidgets) (3.0.52)
Requirement already satisfied: pygments in /usr/local/lib/python3.12/dist-packages (from ipython&gt;=4.0.0-&gt;ipywidgets) (2.19.2)
Requirement already satisfied: backcall in /usr/local/lib/python3.12/dist-packages (from ipython&gt;=4.0.0-&gt;ipywidgets) (0.2.0)
Requirement already satisfied: pexpect&gt;4.3 in /usr/local/lib/python3.12/dist-packages (from ipython&gt;=4.0.0-&gt;ipywidgets) (4.9.0)
Requirement already satisfied: notebook&gt;=4.4.1 in /usr/local/lib/python3.12/dist-packages (from widgetsnbextension~=3.6.0-&gt;ipywidgets) (6.5.7)
Requirement already satisfied: parso&lt;0.9.0,&gt;=0.8.4 in /usr/local/lib/python3.12/dist-packages (from jedi&gt;=0.16-&gt;ipython&gt;=4.0.0-&gt;ipywidgets) (0.8.6)
Requirement already satisfied: entrypoints in /usr/local/lib/python3.12/dist-packages (from jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets) (0.4)
Requirement already satisfied: jupyter-core&gt;=4.9.2 in /usr/local/lib/python3.12/dist-packages (from jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets) (5.9.1)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in /usr/local/lib/python3.12/dist-packages (from jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets) (2.9.0.post0)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (3.1.6)
Requirement already satisfied: argon2-cffi in /usr/local/lib/python3.12/dist-packages (from notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (25.1.0)
Requirement already satisfied: nbformat in /usr/local/lib/python3.12/dist-packages (from notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (5.10.4)
Requirement already satisfied: nbconvert&gt;=5 in /usr/local/lib/python3.12/dist-packages (from notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (7.17.0)
Requirement already satisfied: Send2Trash&gt;=1.8.0 in /usr/local/lib/python3.12/dist-packages (from notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (2.1.0)
Requirement already satisfied: terminado&gt;=0.8.3 in /usr/local/lib/python3.12/dist-packages (from notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.18.1)
Requirement already satisfied: prometheus-client in /usr/local/lib/python3.12/dist-packages (from notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.24.1)
Requirement already satisfied: nbclassic&gt;=0.4.7 in /usr/local/lib/python3.12/dist-packages (from notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.3.3)
Requirement already satisfied: ptyprocess&gt;=0.5 in /usr/local/lib/python3.12/dist-packages (from pexpect&gt;4.3-&gt;ipython&gt;=4.0.0-&gt;ipywidgets) (0.7.0)
Requirement already satisfied: wcwidth in /usr/local/lib/python3.12/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0-&gt;ipython&gt;=4.0.0-&gt;ipywidgets) (0.6.0)
Requirement already satisfied: platformdirs&gt;=2.5 in /usr/local/lib/python3.12/dist-packages (from jupyter-core&gt;=4.9.2-&gt;jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets) (4.9.4)
Requirement already satisfied: notebook-shim&gt;=0.2.3 in /usr/local/lib/python3.12/dist-packages (from nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.2.4)
Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.12/dist-packages (from nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (4.13.5)
Requirement already satisfied: bleach!=5.0.0 in /usr/local/lib/python3.12/dist-packages (from bleach[css]!=5.0.0-&gt;nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (6.3.0)
Requirement already satisfied: defusedxml in /usr/local/lib/python3.12/dist-packages (from nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.7.1)
Requirement already satisfied: jupyterlab-pygments in /usr/local/lib/python3.12/dist-packages (from nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.3.0)
Requirement already satisfied: markupsafe&gt;=2.0 in /usr/local/lib/python3.12/dist-packages (from nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (3.0.3)
Requirement already satisfied: mistune&lt;4,&gt;=2.0.3 in /usr/local/lib/python3.12/dist-packages (from nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (3.2.0)
Requirement already satisfied: nbclient&gt;=0.5.0 in /usr/local/lib/python3.12/dist-packages (from nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.10.4)
Requirement already satisfied: pandocfilters&gt;=1.4.1 in /usr/local/lib/python3.12/dist-packages (from nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.5.1)
Requirement already satisfied: fastjsonschema&gt;=2.15 in /usr/local/lib/python3.12/dist-packages (from nbformat-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (2.21.2)
Requirement already satisfied: jsonschema&gt;=2.6 in /usr/local/lib/python3.12/dist-packages (from nbformat-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (4.26.0)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil&gt;=2.8.2-&gt;jupyter-client&gt;=6.1.12-&gt;ipykernel&gt;=4.5.1-&gt;ipywidgets) (1.17.0)
Requirement already satisfied: argon2-cffi-bindings in /usr/local/lib/python3.12/dist-packages (from argon2-cffi-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (25.1.0)
Requirement already satisfied: webencodings in /usr/local/lib/python3.12/dist-packages (from bleach!=5.0.0-&gt;bleach[css]!=5.0.0-&gt;nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.5.1)
Requirement already satisfied: tinycss2&lt;1.5,&gt;=1.1.0 in /usr/local/lib/python3.12/dist-packages (from bleach[css]!=5.0.0-&gt;nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.4.0)
Requirement already satisfied: attrs&gt;=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=2.6-&gt;nbformat-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (25.4.0)
Requirement already satisfied: jsonschema-specifications&gt;=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=2.6-&gt;nbformat-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (2025.9.1)
Requirement already satisfied: referencing&gt;=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=2.6-&gt;nbformat-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.37.0)
Requirement already satisfied: rpds-py&gt;=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema&gt;=2.6-&gt;nbformat-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.30.0)
Requirement already satisfied: jupyter-server&lt;3,&gt;=1.8 in /usr/local/lib/python3.12/dist-packages (from notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (2.14.0)
Requirement already satisfied: cffi&gt;=1.0.1 in /usr/local/lib/python3.12/dist-packages (from argon2-cffi-bindings-&gt;argon2-cffi-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (2.0.0)
Requirement already satisfied: soupsieve&gt;1.2 in /usr/local/lib/python3.12/dist-packages (from beautifulsoup4-&gt;nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (2.8.3)
Requirement already satisfied: typing-extensions&gt;=4.0.0 in /usr/local/lib/python3.12/dist-packages (from beautifulsoup4-&gt;nbconvert&gt;=5-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (4.15.0)
Requirement already satisfied: pycparser in /usr/local/lib/python3.12/dist-packages (from cffi&gt;=1.0.1-&gt;argon2-cffi-bindings-&gt;argon2-cffi-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (3.0)
Requirement already satisfied: anyio&gt;=3.1.0 in /usr/local/lib/python3.12/dist-packages (from jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (4.12.1)
Requirement already satisfied: jupyter-events&gt;=0.9.0 in /usr/local/lib/python3.12/dist-packages (from jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.12.0)
Requirement already satisfied: jupyter-server-terminals&gt;=0.4.4 in /usr/local/lib/python3.12/dist-packages (from jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.5.4)
Requirement already satisfied: overrides&gt;=5.0 in /usr/local/lib/python3.12/dist-packages (from jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (7.7.0)
Requirement already satisfied: websocket-client&gt;=1.7 in /usr/local/lib/python3.12/dist-packages (from jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.9.0)
Requirement already satisfied: idna&gt;=2.8 in /usr/local/lib/python3.12/dist-packages (from anyio&gt;=3.1.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (3.11)
Requirement already satisfied: python-json-logger&gt;=2.0.4 in /usr/local/lib/python3.12/dist-packages (from jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (4.0.0)
Requirement already satisfied: pyyaml&gt;=5.3 in /usr/local/lib/python3.12/dist-packages (from jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (6.0.3)
Requirement already satisfied: rfc3339-validator in /usr/local/lib/python3.12/dist-packages (from jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.1.4)
Requirement already satisfied: rfc3986-validator&gt;=0.1.1 in /usr/local/lib/python3.12/dist-packages (from jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (0.1.1)
Requirement already satisfied: fqdn in /usr/local/lib/python3.12/dist-packages (from jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.5.1)
Requirement already satisfied: isoduration in /usr/local/lib/python3.12/dist-packages (from jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (20.11.0)
Requirement already satisfied: jsonpointer&gt;1.13 in /usr/local/lib/python3.12/dist-packages (from jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (3.0.0)
Requirement already satisfied: rfc3987-syntax&gt;=1.1.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.1.0)
Requirement already satisfied: uri-template in /usr/local/lib/python3.12/dist-packages (from jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.3.0)
Requirement already satisfied: webcolors&gt;=24.6.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (25.10.0)
Requirement already satisfied: lark&gt;=1.2.2 in /usr/local/lib/python3.12/dist-packages (from rfc3987-syntax&gt;=1.1.0-&gt;jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.3.1)
Requirement already satisfied: arrow&gt;=0.15.0 in /usr/local/lib/python3.12/dist-packages (from isoduration-&gt;jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (1.4.0)
Requirement already satisfied: tzdata in /usr/local/lib/python3.12/dist-packages (from arrow&gt;=0.15.0-&gt;isoduration-&gt;jsonschema[format-nongpl]&gt;=4.18.0-&gt;jupyter-events&gt;=0.9.0-&gt;jupyter-server&lt;3,&gt;=1.8-&gt;notebook-shim&gt;=0.2.3-&gt;nbclassic&gt;=0.4.7-&gt;notebook&gt;=4.4.1-&gt;widgetsnbextension~=3.6.0-&gt;ipywidgets) (2025.3)
Downloading jedi-0.19.2-py2.py3-none-any.whl (1.6 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">1.6/1.6 MB</span><span> </span><span style="color: var(--ansi-red);">16.2 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Installing collected packages: jedi
Successfully installed jedi-0.19.2
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell" id="cell-BHqIxXXcQQX1" role="region" aria-label="Cell 1: Code cell: " style="" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$453401876$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$453401876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$453401876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$453401876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$453401876$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$453401876$--><div class="status">
      <div class="execution-count"><!--?lit$453401876$-->[ ]</div>
      <!--?lit$453401876$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;" tabindex="0"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;pd</span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;ipywidgets&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;widgets</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;IPython.display&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;display</span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;time</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$453401876$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 1 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-ydMBXFKRP2zR" role="region" aria-label="Cell 2: Code cell: " style="" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$453401876$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$453401876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$453401876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$453401876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Kanneganti Lohitha
10:20 PM (13 hours ago)
executed in 6.748s"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$453401876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$453401876$-->executed by Kanneganti Lohitha</div><!----><!----><div><!--?lit$453401876$-->10:20 PM (13 hours ago)</div><!----><!----><div><!--?lit$453401876$-->executed in 6.748s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$453401876$--><div class="status">
      <div class="execution-count"><!--?lit$453401876$-->[ ]</div>
      <!--?lit$453401876$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;" tabindex="0"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;google.colab&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;files</span></span><br><span><span></span></span><br><span><span class="mtk1">uploaded&nbsp;=&nbsp;files.upload()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$453401876$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$453401876$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$453401876$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 56px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./Movie Recommendation Chatbot_files/outputframe.html" class="" style="height: 56px;"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$453401876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$453401876$-->Text
        </md-outlined-button>
        <!--?lit$453401876$-->
        <!--?lit$453401876$-->
      </div><hr>
    </div></div><div class="cell code notebook-cell" id="cell-ucCkZikuP5jT" role="region" aria-label="Cell 3: Code cell: " style="" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$453401876$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$453401876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$453401876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$453401876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$453401876$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$453401876$--><div class="status">
      <div class="execution-count"><!--?lit$453401876$-->[ ]</div>
      <!--?lit$453401876$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;" tabindex="0"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span class="mtk1">df&nbsp;=&nbsp;pd.read_csv(</span><span class="mtk21">'movie_db.csv'</span><span class="mtk1">,&nbsp;encoding=</span><span class="mtk21">'latin-1'</span><span class="mtk1">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$453401876$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 3 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code notebook-cell code-has-output" id="cell-XsnG3fK_P6QP" role="region" aria-label="Cell 4: Code cell: " style="" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$453401876$-->Gemini
    </div><div class="cell-toolbar sticky"></div><div class="main-content"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$453401876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$453401876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$453401876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Kanneganti Lohitha
10:20 PM (13 hours ago)
executed in 0.074s"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$453401876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$453401876$-->executed by Kanneganti Lohitha</div><!----><!----><div><!--?lit$453401876$-->10:20 PM (13 hours ago)</div><!----><!----><div><!--?lit$453401876$-->executed in 0.074s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$453401876$--><div class="status">
      <div class="execution-count"><!--?lit$453401876$-->[ ]</div>
      <!--?lit$453401876$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;" tabindex="0"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span class="mtk1">df[</span><span class="mtk21">'Genre'</span><span class="mtk1">]&nbsp;=&nbsp;df[</span><span class="mtk21">'Genre'</span><span class="mtk1">].</span><span class="mtk14">str</span><span class="mtk1">.lower()</span></span><br><span><span class="mtk1">df[</span><span class="mtk21">'Language'</span><span class="mtk1">]&nbsp;=&nbsp;df[</span><span class="mtk21">'Language'</span><span class="mtk1">].</span><span class="mtk14">str</span><span class="mtk1">.lower()</span></span><br><span><span class="mtk1">df[</span><span class="mtk21">'Movie'</span><span class="mtk1">]&nbsp;=&nbsp;df[</span><span class="mtk21">'Movie'</span><span class="mtk1">].</span><span class="mtk14">str</span><span class="mtk1">.title()</span></span><br><span><span></span></span><br><span><span class="mtk1">greetings&nbsp;=&nbsp;[</span><span class="mtk21">'hi'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'hello'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'hey'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'namaste'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'hola'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'hai'</span><span class="mtk1">]</span></span><br><span><span class="mtk1">thanks_keywords&nbsp;=&nbsp;[</span><span class="mtk21">'thanks'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'thank&nbsp;you'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'thank&nbsp;u'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'thx'</span><span class="mtk1">]</span></span><br><span><span></span></span><br><span><span class="mtk1">chat_output&nbsp;=&nbsp;widgets.Output(layout=widgets.Layout</span><span class="mtk1">(border=</span><span class="mtk21">'1px&nbsp;solid&nbsp;gray'</span><span class="mtk1">,&nbsp;height=</span><span class="mtk21">'300px'</span><span class="mtk1">,&nbsp;overflow=</span><span class="mtk21">'auto'</span><span class="mtk1">))</span></span><br><span><span class="mtk1">user_input&nbsp;=&nbsp;widgets.Text(placeholder=</span><span class="mtk21">'Type&nbsp;your&nbsp;message&nbsp;here&nbsp;and&nbsp;press&nbsp;Enter'</span><span class="mtk1">,&nbsp;description=</span><span class="mtk21">'You:'</span><span class="mtk1">,&nbsp;layout=widgets.Layout(width=</span><span class="mtk21">'80%'</span><span class="mtk1">))</span></span><br><span><span></span></span><br><span><span class="mtk1">enter_button&nbsp;=&nbsp;widgets.Button(description=</span><span class="mtk21">'Enter'</span><span class="mtk1">,&nbsp;button_style=</span><span class="mtk21">'success'</span><span class="mtk1">,&nbsp;layout=widgets.Layout(width=</span><span class="mtk21">'10%'</span><span class="mtk1">))</span></span><br><span><span class="mtk1">clear_button&nbsp;=&nbsp;widgets.Button(description=</span><span class="mtk21">'Clear&nbsp;Chat'</span><span class="mtk1">,&nbsp;button_style=</span><span class="mtk21">'warning'</span><span class="mtk1">,&nbsp;layout=widgets.Layout(width=</span><span class="mtk21">'10%'</span><span class="mtk1">))</span></span><br><span><span class="mtk1">input_box&nbsp;=&nbsp;widgets.HBox([user_input,&nbsp;enter_button</span><span class="mtk1">,&nbsp;clear_button])</span></span><br><span><span></span></span><br><span><span class="mtk1">session&nbsp;=&nbsp;{</span><span class="mtk21">"genre"</span><span class="mtk1">:&nbsp;</span><span class="mtk6">None</span><span class="mtk1">,&nbsp;</span><span class="mtk21">"language"</span><span class="mtk1">:&nbsp;</span><span class="mtk6">None</span><span class="mtk1">}</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Helper&nbsp;extraction&nbsp;functions</span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">extract_genre</span><span class="mtk1">(</span><span class="mtk16">text</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;text_lower&nbsp;=&nbsp;text.lower()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;genre&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;df[</span><span class="mtk21">'Genre'</span><span class="mtk1">].unique():</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;genre&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;text_lower:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;genre</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;</span><span class="mtk6">None</span></span><br><span><span></span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">extract_language</span><span class="mtk1">(</span><span class="mtk16">text</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;text_lower&nbsp;=&nbsp;text.lower()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;lang&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;df[</span><span class="mtk21">'Language'</span><span class="mtk1">].unique():</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;lang&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;text_lower:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;lang</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;</span><span class="mtk6">None</span></span><br><span><span></span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">extract_number</span><span class="mtk1">(</span><span class="mtk16">text</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;words&nbsp;=&nbsp;text.lower().split()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;word&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;words:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;word.isdigit():</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;</span><span class="mtk14">int</span><span class="mtk1">(word)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;</span><span class="mtk6">None</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Recommendation&nbsp;logic</span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">recommend_movies</span><span class="mtk1">(</span><span class="mtk16">genre</span><span class="mtk1">,&nbsp;</span><span class="mtk16">language</span><span class="mtk1">,&nbsp;</span><span class="mtk16">top_n</span><span class="mtk1">=</span><span class="mtk12">3</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;filtered&nbsp;=&nbsp;df[(df[</span><span class="mtk21">'Genre'</span><span class="mtk1">]&nbsp;==&nbsp;genre)&nbsp;&amp;&nbsp;(df[</span><span class="mtk21">'Language'</span><span class="mtk1">]&nbsp;==&nbsp;language)].copy()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;filtered.empty:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"No&nbsp;movies&nbsp;found&nbsp;for&nbsp;genre&nbsp;'</span><span class="mtk1">{genre}</span><span class="mtk21">'&nbsp;and&nbsp;language&nbsp;'</span><span class="mtk1">{language}</span><span class="mtk21">'."</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;top_movies&nbsp;=&nbsp;filtered.sort_values(by=</span><span class="mtk21">'Rating'</span><span class="mtk1">,&nbsp;ascending=</span><span class="mtk6">False</span><span class="mtk1">).head(top_n)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;response&nbsp;=&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"Top&nbsp;</span><span class="mtk1">{</span><span class="mtk15">min</span><span class="mtk1">(top_n,&nbsp;</span><span class="mtk15">len</span><span class="mtk1">(top_movies))}</span><span class="mtk21">&nbsp;</span><span class="mtk1">{genre.title()}</span><span class="mtk21">&nbsp;movies&nbsp;in&nbsp;</span><span class="mtk1">{language.title()}</span><span class="mtk21">:\n"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;_,&nbsp;row&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;top_movies.iterrows():</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;response&nbsp;+=&nbsp;</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;</span><span class="mtk1">{row[</span><span class="mtk21">'Movie'</span><span class="mtk1">]}</span><span class="mtk21">&nbsp;(Rating:&nbsp;</span><span class="mtk1">{row[</span><span class="mtk21">'Rating'</span><span class="mtk1">]}</span><span class="mtk21">)\n"</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;response</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Chat&nbsp;display</span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">print_user_message</span><span class="mtk1">(</span><span class="mtk16">msg</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">with</span><span class="mtk1">&nbsp;chat_output:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk6">f</span><span class="mtk21">"🧑:&nbsp;</span><span class="mtk1">{msg}</span><span class="mtk21">\n"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">print_bot_message</span><span class="mtk1">(</span><span class="mtk16">msg</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">with</span><span class="mtk1">&nbsp;chat_output:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk21">"🤖&nbsp;is&nbsp;typing..."</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(</span><span class="mtk12">1</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">with</span><span class="mtk1">&nbsp;chat_output:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk6">f</span><span class="mtk21">"🤖:&nbsp;</span><span class="mtk1">{msg}</span><span class="mtk21">\n"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Core&nbsp;logic</span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">process_message</span><span class="mtk1">(</span><span class="mtk16">user_msg</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;user_msg&nbsp;=&nbsp;user_msg.strip()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;user_msg:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;print_user_message(user_msg)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;lower_msg&nbsp;=&nbsp;user_msg.lower()</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;lower_msg&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;[</span><span class="mtk21">'quit'</span><span class="mtk1">,&nbsp;</span><span class="mtk21">'exit'</span><span class="mtk1">]:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print_bot_message(</span><span class="mtk21">"Goodbye!&nbsp;👋&nbsp;Have&nbsp;a&nbsp;great&nbsp;day!&nbsp;You&nbsp;can&nbsp;restart&nbsp;the&nbsp;</span><span class="mtk21">chat&nbsp;anytime."</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"genre"</span><span class="mtk1">]&nbsp;=&nbsp;</span><span class="mtk6">None</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">]&nbsp;=&nbsp;</span><span class="mtk6">None</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span></span><br><span><span></span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;lower_msg&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;greetings:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print_bot_message(</span><span class="mtk21">"Hello!&nbsp;👋&nbsp;Tell&nbsp;me&nbsp;a&nbsp;movie&nbsp;genre&nbsp;and&nbsp;language&nbsp;you&nbsp;</span><span class="mtk21">prefer,&nbsp;or&nbsp;just&nbsp;one&nbsp;and&nbsp;I'll&nbsp;ask&nbsp;for&nbsp;the&nbsp;other."</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk15">any</span><span class="mtk1">(thx&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;lower_msg&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;thx&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;thanks_keywords):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print_bot_message(</span><span class="mtk21">"You're&nbsp;welcome!&nbsp;😊&nbsp;Want&nbsp;more&nbsp;recommendations?&nbsp;</span><span class="mtk21">Just&nbsp;say&nbsp;a&nbsp;genre&nbsp;or&nbsp;language."</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"genre"</span><span class="mtk1">]&nbsp;=&nbsp;</span><span class="mtk6">None</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">]&nbsp;=&nbsp;</span><span class="mtk6">None</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;genre&nbsp;=&nbsp;extract_genre(user_msg)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;language&nbsp;=&nbsp;extract_language(user_msg)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;genre:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"genre"</span><span class="mtk1">]&nbsp;=&nbsp;genre</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;language:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">]&nbsp;=&nbsp;language</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;num_movies&nbsp;=&nbsp;extract_number(user_msg)&nbsp;</span><span class="mtk6">or</span><span class="mtk1">&nbsp;</span><span class="mtk12">3</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;session[</span><span class="mtk21">"genre"</span><span class="mtk1">]&nbsp;</span><span class="mtk6">and</span><span class="mtk1">&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">]:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;response&nbsp;=&nbsp;recommend_movies(session[</span><span class="mtk21">"genre"</span><span class="mtk1">],&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">],&nbsp;num_movies)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print_bot_message(response)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"genre"</span><span class="mtk1">],&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">]&nbsp;=&nbsp;</span><span class="mtk6">None</span><span class="mtk1">,&nbsp;</span><span class="mtk6">None</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">elif</span><span class="mtk1">&nbsp;session[</span><span class="mtk21">"genre"</span><span class="mtk1">]:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;available_langs&nbsp;=&nbsp;</span><span class="mtk21">',&nbsp;'</span><span class="mtk1">.join(df[df[</span><span class="mtk21">'Genre'</span><span class="mtk1">]&nbsp;==&nbsp;session[</span><span class="mtk21">"genre"</span><span class="mtk1">]][</span><span class="mtk21">'Language'</span><span class="mtk1">].unique())</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print_bot_message(</span><span class="mtk6">f</span><span class="mtk21">"Great!&nbsp;Which&nbsp;language&nbsp;do&nbsp;you&nbsp;prefer?&nbsp;Available&nbsp;fo</span><span class="mtk21">r&nbsp;</span><span class="mtk1">{session[</span><span class="mtk21">'genre'</span><span class="mtk1">].title()}</span><span class="mtk21">:&nbsp;</span><span class="mtk1">{available_langs}</span><span class="mtk21">"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">elif</span><span class="mtk1">&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">]:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;available_genres&nbsp;=&nbsp;</span><span class="mtk21">',&nbsp;'</span><span class="mtk1">.join(df[df[</span><span class="mtk21">'Language'</span><span class="mtk1">]&nbsp;==&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">]][</span><span class="mtk21">'Genre'</span><span class="mtk1">].unique())</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print_bot_message(</span><span class="mtk6">f</span><span class="mtk21">"You&nbsp;chose&nbsp;</span><span class="mtk1">{session[</span><span class="mtk21">'language'</span><span class="mtk1">].title()}</span><span class="mtk21">&nbsp;language.&nbsp;Which&nbsp;genre&nbsp;do&nbsp;you&nbsp;like?&nbsp;Available&nbsp;genr</span><span class="mtk21">es:&nbsp;</span><span class="mtk1">{available_genres}</span><span class="mtk21">"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print_bot_message(</span><span class="mtk21">"Please&nbsp;mention&nbsp;a&nbsp;genre&nbsp;and&nbsp;language&nbsp;like&nbsp;'romance</span><span class="mtk21">&nbsp;in&nbsp;Hindi'&nbsp;or&nbsp;'action&nbsp;Telugu&nbsp;movies'."</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Events</span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">on_enter_clicked</span><span class="mtk1">(</span><span class="mtk16">b</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;process_message(user_input.value)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;user_input.value&nbsp;=&nbsp;</span><span class="mtk21">''</span></span><br><span><span></span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">on_clear_clicked</span><span class="mtk1">(</span><span class="mtk16">b</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;chat_output.clear_output()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"genre"</span><span class="mtk1">]&nbsp;=&nbsp;</span><span class="mtk6">None</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;session[</span><span class="mtk21">"language"</span><span class="mtk1">]&nbsp;=&nbsp;</span><span class="mtk6">None</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">with</span><span class="mtk1">&nbsp;chat_output:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk21">"🤖:&nbsp;Chat&nbsp;cleared.&nbsp;Say&nbsp;hi&nbsp;to&nbsp;start&nbsp;a&nbsp;new&nbsp;</span><span class="mtk21">conversation!\n"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">on_text_submit</span><span class="mtk1">(</span><span class="mtk16">change</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;process_message(change.value)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;user_input.value&nbsp;=&nbsp;</span><span class="mtk21">''</span></span><br><span><span></span></span><br><span><span class="mtk1">enter_button.on_click(on_enter_clicked)</span></span><br><span><span class="mtk1">clear_button.on_click(on_clear_clicked)</span></span><br><span><span class="mtk1">user_input.on_submit(on_text_submit)</span></span><br><span><span></span></span><br><span><span class="mtk1">display(chat_output,&nbsp;input_box)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$453401876$-->Start coding or <span role="button" class="link" tabindex="0">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area"></div></colab-form></div>
    <div class="output" aria-label="Cell 4 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><!--?lit$453401876$--><md-icon-button toggle="" class="toggle-visibility-button" touch-target="none" data-aria-label="Show/hide output" id="toggle-visibility-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show/hide output" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-visibility-button" message="Show/hide output"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Show/hide output</div><!----><!--?--></template></colab-tooltip-trigger><!--?lit$453401876$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" class="menu-button" data-aria-label="Code cell output actions" id="menu-button" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="menu-button" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 351px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./Movie Recommendation Chatbot_files/outputframe(1).html" class="" style="height: 351px;"></iframe></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$453401876$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$453401876$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$453401876$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-scroller>
    </div><div class="right-pane-snap-hint"></div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$453401876$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$453401876$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-2-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$453401876$--><md-icon-button id="tab-pane-2-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$453401876$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$453401876$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$453401876$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-1-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$453401876$--><md-icon-button id="tab-pane-1-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$453401876$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <div class="tab-pane-header-actions"></div>
      <!--?lit$453401876$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-3-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$453401876$--><md-icon-button id="tab-pane-3-close-all-button" data-aria-label="Close all tabs" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close all tabs">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-close-all-button" message="Close all tabs"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Close all tabs</div><!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./Movie Recommendation Chatbot_files/outputframe(2).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./Movie Recommendation Chatbot_files/outputframe(3).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer-floating-spark><template shadowrootmode="open"><!---->
      <md-icon-button toggle="" id="toggle-composer-button" data-aria-label="Toggle Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini" aria-pressed="false">
        <!--?lit$453401876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$453401876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$453401876$--><span class="icon"><slot></slot></span>
        <!--?lit$453401876$-->
        <!--?lit$453401876$--><span class="touch"></span>
  </button></template>
        <!--?lit$453401876$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer-button" message="Toggle Gemini"><template shadowrootmode="open"><!----><!--?lit$453401876$--><!----><div><!--?lit$453401876$-->Toggle Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template></colab-composer-floating-spark><colab-status-bar role="region" aria-label="Runtime status bar"><template shadowrootmode="open"><!----><span class="left">
        <slot name="bottom-pane-buttons"></slot>
      </span>
      <span class="right">
        <!--?lit$453401876$--><colab-execution-status><template shadowrootmode="open"><!----></template></colab-execution-status><!--?lit$453401876$--><!--?lit$453401876$--><!--?lit$453401876$--><colab-runtime-status><template shadowrootmode="open"><!----></template></colab-runtime-status>
      </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->data_object</md-icon>
        <!--?lit$453401876$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$453401876$-->terminal</md-icon>
        <!--?lit$453401876$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 663px; visibility: visible; left: 70px; top: 62px; display: none;"><!--?lit$453401876$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Locate in Drive<!--?lit$453401876$--></div></div><div command="open-in-playground" class="goog-menuitem" role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Open in playground mode<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class="goog-menuitem" role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->New notebook in Drive<!--?lit$453401876$--></div></div><div command="open" class="goog-menuitem" role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Open notebook<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class="goog-menuitem" role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Upload notebook<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class="goog-menuitem" role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Rename<!--?lit$453401876$--></div></div><div command="move-notebook" class="goog-menuitem" role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Move<!--?lit$453401876$--></div></div><div command="trash" class="goog-menuitem" role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Move to trash<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class="goog-menuitem" role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Save a copy in Drive<!--?lit$453401876$--></div></div><div command="copy-to-gist" class="goog-menuitem" role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Save a copy as a GitHub Gist<!--?lit$453401876$--></div></div><div command="copy-to-github" class="goog-menuitem" role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Save a copy in GitHub<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class="goog-menuitem" role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Save<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Save and pin revision<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Revision history<!--?lit$453401876$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Notebook info<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":l" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$453401876$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Print<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$453401876$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Download .ipynb<!--?lit$453401876$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Download .py<!--?lit$453401876$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 663px; visibility: visible; left: 108.8px; top: 62px; display: none;"><!--?lit$453401876$--><div command="undo" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":r" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">Undo<span class="goog-menuitem-accel">Ctrl+M Z</span></div></div><div command="redo" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":s" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">Redo<span class="goog-menuitem-accel">Ctrl+Shift+Y</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":t" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Select all cells<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+Shift+A</span></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Cut cell or selection<!--?lit$453401876$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Copy cell or selection<!--?lit$453401876$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Paste<!--?lit$453401876$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Delete selected cells<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+M D</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":z" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Find and replace<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+H</span></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Find next<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+G</span></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":12" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Find previous<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+Shift+G</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":13" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":14" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Notebook settings<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":15" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":16" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Clear all outputs<!--?lit$453401876$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 663px; visibility: visible; left: 150.338px; top: 62px; display: none;"><!--?lit$453401876$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----> </div><!--?lit$453401876$-->Table of contents<!--?lit$453401876$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Executed code history<!--?lit$453401876$--></div></div><div command="start-presentation" class=" goog-menuitem " role="menuitem" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Start slideshow<!--?lit$453401876$--><span class="goog-menuitem-accel">Alt+V</span></div></div><div command="start-presentation-beginning" class=" goog-menuitem " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Start slideshow from beginning<!--?lit$453401876$--><span class="goog-menuitem-accel">Alt+Shift+V</span></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$453401876$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1g" style="user-select: none;"></div><div command="collapse-sections" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1h" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Collapse sections<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+]</span></div></div><div command="expand-sections" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1i" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Expand sections<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+[</span></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none; display: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Save collapsed section layout<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1k" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Show/hide code<!--?lit$453401876$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Show/hide output<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+M O</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1n" style="user-select: none;"></div><div command="focus-next-tab" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1o" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Focus next tab<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+Shift+]</span></div></div><div command="focus-previous-tab" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1p" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Focus previous tab<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+Shift+[</span></div></div><div command="move-tab-to-next" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1q" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Move tab to next pane<!--?lit$453401876$--></div></div><div command="move-tab-to-prev" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1r" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Move tab to previous pane<!--?lit$453401876$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$453401876$--><div command="hide-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option" role="menuitemradio" id=":1d" aria-checked="false" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"></div><!--?lit$453401876$-->Hide comments<!--?lit$453401876$--></div></div><div command="show-minimized-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option" role="menuitemradio" id=":1e" aria-checked="false" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"></div><!--?lit$453401876$-->Minimize comments<!--?lit$453401876$--></div></div><div command="show-expanded-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option goog-option-selected" role="menuitemradio" id=":1f" aria-checked="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$453401876$-->Expand comments<!--?lit$453401876$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 663px; visibility: visible; left: 197.562px; top: 62px; display: none;"><!--?lit$453401876$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Code cell<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+M B</span></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Text cell<!--?lit$453401876$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Section header cell<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1w" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Scratch code cell<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+Alt+N</span></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Code snippets<!--?lit$453401876$--><span class="goog-menuitem-accel">Ctrl+Alt+P</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1z" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Add a form field<!--?lit$453401876$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$453401876$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Run all<!--?lit$453401876$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Run before<!--?lit$453401876$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Run the focused cell<!--?lit$453401876$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Run selection<!--?lit$453401876$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Run cell and below<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Interrupt execution<!--?lit$453401876$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Restart session<!--?lit$453401876$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Restart session and run all<!--?lit$453401876$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Disconnect and delete runtime<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Change runtime type<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2e" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Manage sessions<!--?lit$453401876$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->View resources<!--?lit$453401876$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->View runtime logs<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="deploy-cloud-run" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Deploy to Google Cloud Run<!--?lit$453401876$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$453401876$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Command palette<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2m" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Settings<!--?lit$453401876$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Keyboard shortcuts<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2p" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Diff notebooks<!--?lit$453401876$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$453401876$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$453401876$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Frequently asked questions<!--?lit$453401876$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->View release notes<!--?lit$453401876$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Search code snippets<!--?lit$453401876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2v" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Report a bug<!--?lit$453401876$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Report Drive abuse<!--?lit$453401876$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->Send feedback<!--?lit$453401876$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$453401876$-->View terms of service<!--?lit$453401876$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$453401876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$453401876$--><button id="button" class="button">
      <!--?lit$453401876$-->
      <span class="touch"></span>
      <!--?lit$453401876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$453401876$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$453401876$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy443a3c9ea2a534e0328236aa77177d1d0842a5ca0.3386607344" name="apiproxy443a3c9ea2a534e0328236aa77177d1d0842a5ca0.3386607344" src="./Movie Recommendation Chatbot_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-ghubt3714uy6" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./Movie Recommendation Chatbot_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./Movie Recommendation Chatbot_files/saved_resource.html"></iframe></div><iframe src="./Movie Recommendation Chatbot_files/bscframe.html" style="display: none;"></iframe></body></html>