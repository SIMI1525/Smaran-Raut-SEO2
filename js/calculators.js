/**
 * Interactive Utility & Centerpiece Calculators
 * All calculations and DOM bindings are error-isolated with try...catch blocks.
 * Provides instant reactivity, technical metric estimates, status badges, and dynamic advice.
 * Note: Exact fees are never displayed publicly; estimates focus on scope, technical readiness, and inquiry potential.
 */

const Calculators = {
  // Format currency helpers (preserved for backwards-compatibility)
  formatNPR: function(amount) {
    try {
      return "NPR " + Math.round(amount).toLocaleString('en-IN');
    } catch (e) {
      return "NPR " + amount;
    }
  },

  formatUSD: function(amount) {
    try {
      return "$" + Math.round(amount).toLocaleString('en-US');
    } catch (e) {
      return "$" + amount;
    }
  },

  // 1. Local SEO Visibility & Citations Auditor
  initLocalSeoCalculator: function() {
    try {
      const container = document.getElementById('local-seo-calculator');
      if (!container) return;

      const reviewInput = container.querySelector('#lseo-reviews');
      const gbpRating = container.querySelector('#lseo-rating');
      const citationsInput = container.querySelector('#lseo-citations');
      const radiusInput = container.querySelector('#lseo-radius');

      const scoreEl = container.querySelector('#lseo-score');
      const rankBadge = container.querySelector('#lseo-rank-badge');
      const callsEl = container.querySelector('#lseo-projected-calls');
      const revenueEl = container.querySelector('#lseo-projected-rev');
      const adviceEl = container.querySelector('#lseo-advice');

      function calculate() {
        try {
          const reviews = parseInt(reviewInput ? reviewInput.value : 15, 10) || 0;
          const rating = parseFloat(gbpRating ? gbpRating.value : 4.2) || 1.0;
          const citations = parseInt(citationsInput ? citationsInput.value : 20, 10) || 0;
          const radiusKm = parseInt(radiusInput ? radiusInput.value : 5, 10) || 1;

          // Update label displays
          const rLab = container.querySelector('#lseo-reviews-val');
          if (rLab) rLab.textContent = reviews;
          const citLab = container.querySelector('#lseo-citations-val');
          if (citLab) citLab.textContent = citations;

          // Score out of 100
          let score = Math.min(100, Math.round(
            (reviews * 0.7) + 
            ((rating / 5) * 30) + 
            (citations * 0.8) + 
            (radiusKm > 5 ? 10 : 5)
          ));

          if (scoreEl) scoreEl.textContent = score + "/100";

          let status = "";
          let badgeClass = "";
          let monthlyCalls = Math.round(score * 1.8 + reviews * 0.5);

          if (score < 40) {
            status = "Low Visibility (Invisible in Local 3-Pack)";
            badgeClass = "badge-danger";
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Action Needed:</strong> Your business has limited visibility in local Google Maps searches. Priority steps: verify your physical business address, gather authentic customer reviews, and ensure consistent Name, Address, and Phone listings.";
            }
          } else if (score < 75) {
            status = "Moderate Competitiveness (Occasional 3-Pack)";
            badgeClass = "badge-gold";
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Opportunity:</strong> You have moderate local search signals. Adding LocalBusiness structured data, updating business photos, and keeping opening hours accurate will help secure consistent local map rankings.";
            }
          } else {
            status = "Strong Local Authority (Map Pack Contender)";
            badgeClass = "badge-teal";
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Strong Presence:</strong> Your local trust signals are well-established. Your business is well-positioned for local searches in Itahari, Dharan, and Biratnagar.";
            }
          }

          if (rankBadge) {
            rankBadge.textContent = status;
            rankBadge.className = "badge " + badgeClass;
          }

          if (callsEl) callsEl.textContent = "~" + monthlyCalls + " Inquiries/mo";
          if (revenueEl) revenueEl.textContent = score >= 75 ? "High Local Readiness" : (score >= 40 ? "Moderate Local Readiness" : "Foundational Readiness");
        } catch (innerErr) {
          console.error("Local SEO calc error:", innerErr);
        }
      }

      const inputs = [reviewInput, gbpRating, citationsInput, radiusInput];
      inputs.forEach(input => {
        if (input) {
          input.addEventListener('input', calculate);
          input.addEventListener('change', calculate);
        }
      });

      calculate();
    } catch (e) {
      console.warn("Error initializing local SEO calculator:", e);
    }
  },

  // 2. Web Development Scope & Structure Planner
  initWebDevBudgetCalculator: function() {
    try {
      const container = document.getElementById('webdev-budget-calculator');
      if (!container) return;

      const siteTypeSelect = container.querySelector('#wdev-type');
      const pagesSlider = container.querySelector('#wdev-pages');
      const speedSelect = container.querySelector('#wdev-speed');
      const cmsSelect = container.querySelector('#wdev-cms');

      const pagesVal = container.querySelector('#wdev-pages-val');
      const timelineEl = container.querySelector('#wdev-timeline');
      const budgetNprEl = container.querySelector('#wdev-budget-npr');
      const budgetUsdEl = container.querySelector('#wdev-budget-usd');
      const scoreBadge = container.querySelector('#wdev-score-badge');
      const adviceEl = container.querySelector('#wdev-advice');

      function calculate() {
        try {
          const type = siteTypeSelect ? siteTypeSelect.value : 'corporate';
          const pages = parseInt(pagesSlider ? pagesSlider.value : 10, 10) || 5;
          const speed = speedSelect ? speedSelect.value : 'fast';

          if (pagesVal) pagesVal.textContent = pages + " pages";

          if (timelineEl) timelineEl.textContent = "Advance + Completion Balance";
          if (budgetNprEl) budgetNprEl.textContent = "Milestone Payment Structure";
          if (budgetUsdEl) budgetUsdEl.textContent = "Stage 1: Advance · Stage 2: Completion";

          let cwvScore = speed === 'ultra' ? "100/100 Core Web Vitals" : "90-95/100 Mobile Score";
          if (scoreBadge) {
            scoreBadge.textContent = cwvScore;
            scoreBadge.className = "badge " + (speed === 'ultra' ? "badge-teal" : "badge-gold");
          }

          if (adviceEl) {
            if (type === 'ecommerce') {
              adviceEl.innerHTML = "<strong>Recommended Architecture:</strong> Lightweight online store architecture with structured product schema, responsive mobile catalog views, and smooth checkout flow.";
            } else {
              adviceEl.innerHTML = "<strong>Recommended Architecture:</strong> Clean, pre-rendered static HTML structure. Provides fast mobile loading, clear navigation, and natural search discovery with zero plugin bloat.";
            }
          }
        } catch (innerErr) {
          console.error("Webdev calc error:", innerErr);
        }
      }

      [siteTypeSelect, pagesSlider, speedSelect, cmsSelect].forEach(input => {
        if (input) {
          input.addEventListener('input', calculate);
          input.addEventListener('change', calculate);
        }
      });

      calculate();
    } catch (e) {
      console.warn("Error initializing webdev calculator:", e);
    }
  },

  // 3. Technical SEO Inquiry & Growth Forecaster
  initSeoRoiCalculator: function() {
    try {
      const container = document.getElementById('seo-roi-calculator');
      if (!container) return;

      const sessionsInput = container.querySelector('#roi-sessions');
      const convRateInput = container.querySelector('#roi-cvr');
      const targetGrowth = container.querySelector('#roi-target');

      const sessionsVal = container.querySelector('#roi-sessions-val');
      const cvrVal = container.querySelector('#roi-cvr-val');

      const revGainEl = container.querySelector('#roi-rev-gain');
      const annualGainEl = container.querySelector('#roi-annual-gain');
      const roiMultEl = container.querySelector('#roi-multiplier');
      const adviceEl = container.querySelector('#roi-advice');

      function calculate() {
        try {
          const sessions = parseInt(sessionsInput ? sessionsInput.value : 5000, 10) || 500;
          const cvr = parseFloat(convRateInput ? convRateInput.value : 2.0) || 0.5;
          const multiplier = parseFloat(targetGrowth ? targetGrowth.value : 2.5) || 1.5;

          if (sessionsVal) sessionsVal.textContent = sessions.toLocaleString() + " visits/mo";
          if (cvrVal) cvrVal.textContent = cvr + "%";

          const currentMonthlyConversions = (sessions * (cvr / 100));
          const additionalInquiries = Math.round(currentMonthlyConversions * (multiplier - 1));

          if (revGainEl) revGainEl.textContent = "+" + additionalInquiries + " Inquiries/mo";
          if (annualGainEl) annualGainEl.textContent = "Assessed on 1-Month Activity";
          if (roiMultEl) roiMultEl.textContent = multiplier + "x Organic Growth Target";

          if (adviceEl) {
            adviceEl.innerHTML = "<strong>Search Growth Planning:</strong> Fixing technical errors and improving site structure helps attract qualified customer inquiries. After 1 month of live website activity, traffic and click data are reviewed to evaluate actual search response.";
          }
        } catch (innerErr) {
          console.error("SEO ROI calc error:", innerErr);
        }
      }

      [sessionsInput, convRateInput, targetGrowth].forEach(input => {
        if (input) {
          input.addEventListener('input', calculate);
          input.addEventListener('change', calculate);
        }
      });

      calculate();
    } catch (e) {
      console.warn("Error initializing SEO ROI calculator:", e);
    }
  },

  // 4. Core Web Vitals Speed Impact Simulator
  initCwvSpeedCalculator: function() {
    try {
      const container = document.getElementById('cwv-speed-calculator');
      if (!container) return;

      const lcpInput = container.querySelector('#cwv-lcp');
      const inpInput = container.querySelector('#cwv-inp');
      const clsInput = container.querySelector('#cwv-cls');

      const lcpVal = container.querySelector('#cwv-lcp-val');
      const inpVal = container.querySelector('#cwv-inp-val');
      const clsVal = container.querySelector('#cwv-cls-val');

      const statusBadge = container.querySelector('#cwv-status-badge');
      const bounceRiskEl = container.querySelector('#cwv-bounce-risk');
      const cvrUpliftEl = container.querySelector('#cwv-cvr-uplift');
      const adviceEl = container.querySelector('#cwv-advice');

      function calculate() {
        try {
          const lcp = parseFloat(lcpInput ? lcpInput.value : 4.2) || 1.0;
          const inp = parseInt(inpInput ? inpInput.value : 350, 10) || 50;
          const cls = parseFloat(clsInput ? clsInput.value : 0.18) || 0.01;

          if (lcpVal) lcpVal.textContent = lcp.toFixed(1) + "s";
          if (inpVal) inpVal.textContent = inp + "ms";
          if (clsVal) clsVal.textContent = cls.toFixed(2);

          const passLCP = lcp <= 2.5;
          const passINP = inp <= 200;
          const passCLS = cls <= 0.1;

          let status = "";
          let badgeClass = "";
          let bouncePenalty = 0;
          let cvrUplift = 0;

          if (passLCP && passINP && passCLS) {
            status = "GOOD (Passed All Google Core Web Vitals)";
            badgeClass = "badge-teal";
            bouncePenalty = 8;
            cvrUplift = 0;
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Speed Superiority:</strong> Your site ranks in the top bracket for performance. Search engines reward fast rendering with smooth indexing and good user experience.";
            }
          } else if (lcp > 4.0 || inp > 400 || cls > 0.25) {
            status = "POOR (Mobile Experience Needs Improvement)";
            badgeClass = "badge-danger";
            bouncePenalty = Math.round((lcp - 2.5) * 18 + (inp > 300 ? 15 : 5));
            cvrUplift = Math.min(38, Math.round((lcp - 2.0) * 8.5));
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Conversion Opportunity:</strong> Slow mobile paint times and layout shifts cause mobile users to leave. Optimizing image sizes and cleaning scripts improves user engagement.";
            }
          } else {
            status = "NEEDS IMPROVEMENT (Sub-optimal UX)";
            badgeClass = "badge-gold";
            bouncePenalty = Math.round((lcp - 2.5) * 12 + 10);
            cvrUplift = Math.round((lcp - 2.0) * 5.5);
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Opportunity:</strong> Your site is close to meeting recommended thresholds. Compressing hero photos and deferring non-critical scripts will push your pages into the optimal speed bracket.";
            }
          }

          if (statusBadge) {
            statusBadge.textContent = status;
            statusBadge.className = "badge " + badgeClass;
          }

          if (bounceRiskEl) bounceRiskEl.textContent = "+" + Math.max(0, bouncePenalty) + "% Mobile Bounce Risk";
          if (cvrUpliftEl) cvrUpliftEl.textContent = "+" + Math.max(2, cvrUplift) + "% Projected Interaction Lift";
        } catch (innerErr) {
          console.error("CWV calc error:", innerErr);
        }
      }

      [lcpInput, inpInput, clsInput].forEach(input => {
        if (input) {
          input.addEventListener('input', calculate);
          input.addEventListener('change', calculate);
        }
      });

      calculate();
    } catch (e) {
      console.warn("Error initializing CWV calculator:", e);
    }
  },

  // 5. E-Commerce Checkout Retention Simulator
  initEcommerceLossCalculator: function() {
    try {
      const container = document.getElementById('ecommerce-loss-calculator');
      if (!container) return;

      const trafficInput = container.querySelector('#ecom-traffic');
      const loadTimeInput = container.querySelector('#ecom-loadtime');

      const trafficVal = container.querySelector('#ecom-traffic-val');
      const loadTimeVal = container.querySelector('#ecom-loadtime-val');

      const lostMonthlyEl = container.querySelector('#ecom-lost-monthly');
      const lostAnnualEl = container.querySelector('#ecom-lost-annual');
      const recoveryEl = container.querySelector('#ecom-recovery');
      const adviceEl = container.querySelector('#ecom-advice');

      function calculate() {
        try {
          const traffic = parseInt(trafficInput ? trafficInput.value : 12000, 10) || 1000;
          const loadTime = parseFloat(loadTimeInput ? loadTimeInput.value : 4.5) || 1.0;

          if (trafficVal) trafficVal.textContent = traffic.toLocaleString() + " visits/mo";
          if (loadTimeVal) loadTimeVal.textContent = loadTime.toFixed(1) + "s";

          const speedPenaltyRatio = Math.max(0, (loadTime - 1.8) * 0.006);
          const lostOrders = Math.round(traffic * speedPenaltyRatio);

          if (lostMonthlyEl) lostMonthlyEl.textContent = "~" + lostOrders + " Drop-Offs/mo";
          if (lostAnnualEl) lostAnnualEl.textContent = "Mobile Cart Friction Identified";
          if (recoveryEl) recoveryEl.textContent = "+" + lostOrders + " Potential Completed Orders";

          if (adviceEl) {
            adviceEl.innerHTML = "<strong>Performance Optimization:</strong> By optimizing image formats, streamlining product code, and organizing categories cleanly, online stores reduce mobile drop-offs and make browsing effortless for shoppers.";
          }
        } catch (innerErr) {
          console.error("E-com calc error:", innerErr);
        }
      }

      [trafficInput, loadTimeInput].forEach(input => {
        if (input) {
          input.addEventListener('input', calculate);
          input.addEventListener('change', calculate);
        }
      });

      calculate();
    } catch (e) {
      console.warn("Error initializing ecommerce calculator:", e);
    }
  },

  // 6. Topical Authority Gap Scorer
  initTopicalGapCalculator: function() {
    try {
      const container = document.getElementById('topical-gap-calculator');
      if (!container) return;

      const pillarsInput = container.querySelector('#tgap-pillars');
      const clustersInput = container.querySelector('#tgap-clusters');
      const linksInput = container.querySelector('#tgap-links');
      const schemaCheck = container.querySelector('#tgap-schema');

      const scoreEl = container.querySelector('#tgap-score');
      const authorityBadge = container.querySelector('#tgap-authority-badge');
      const indexVelocityEl = container.querySelector('#tgap-velocity');
      const adviceEl = container.querySelector('#tgap-advice');

      function calculate() {
        try {
          const pillars = parseInt(pillarsInput ? pillarsInput.value : 3, 10) || 1;
          const clusters = parseInt(clustersInput ? clustersInput.value : 12, 10) || 0;
          const linksPerArticle = parseInt(linksInput ? linksInput.value : 4, 10) || 1;
          const hasSchema = schemaCheck ? schemaCheck.checked : true;

          const cLab = container.querySelector('#tgap-clusters-val');
          if (cLab) cLab.textContent = clusters + " articles/pillar";

          let score = Math.min(100, Math.round(
            (pillars * 8) + 
            (clusters * 2.2) + 
            (linksPerArticle * 3.5) + 
            (hasSchema ? 15 : 0)
          ));

          if (scoreEl) scoreEl.textContent = score + "/100";

          let status = "";
          let badgeClass = "";
          let velocity = "";

          if (score < 45) {
            status = "Thin Topical Coverage (Limited Search Presence)";
            badgeClass = "badge-danger";
            velocity = "Developing (Needs additional content)";
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Content Planning:</strong> Your site has limited topic coverage. Creating supporting articles and FAQs around your main services will build search visibility.";
            }
          } else if (score < 80) {
            status = "Developing Topical Cluster (Solid Foundation)";
            badgeClass = "badge-gold";
            velocity = "Steady (Good search discovery)";
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Growth Opportunity:</strong> You have solid core foundations. Adding helpful customer guides and linking related pages together will strengthen topic authority.";
            }
          } else {
            status = "Comprehensive Topic Authority (Strong Presence)";
            badgeClass = "badge-teal";
            velocity = "Fast (Established search presence)";
            if (adviceEl) {
              adviceEl.innerHTML = "<strong>Strong Presence:</strong> Your structured topics and clear internal links help search engines understand your services thoroughly.";
            }
          }

          if (authorityBadge) {
            authorityBadge.textContent = status;
            authorityBadge.className = "badge " + badgeClass;
          }

          if (indexVelocityEl) indexVelocityEl.textContent = velocity;
        } catch (innerErr) {
          console.error("Topical gap calc error:", innerErr);
        }
      }

      [pillarsInput, clustersInput, linksInput, schemaCheck].forEach(input => {
        if (input) {
          input.addEventListener('input', calculate);
          input.addEventListener('change', calculate);
        }
      });

      calculate();
    } catch (e) {
      console.warn("Error initializing topical gap calculator:", e);
    }
  },

  // Master initializer
  initAll: function() {
    this.initLocalSeoCalculator();
    this.initWebDevBudgetCalculator();
    this.initSeoRoiCalculator();
    this.initCwvSpeedCalculator();
    this.initEcommerceLossCalculator();
    this.initTopicalGapCalculator();
  }
};

// Auto-run when DOM is parsed
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', function() {
    Calculators.initAll();
  });
} else {
  Calculators.initAll();
}
