export const site = {
  name: 'Siddhant Morye',
  title: 'Siddhant Morye | Analytics & Operations',
  description:
    'Portfolio of Siddhant Morye, PGDM candidate in Analytics & Operations at Great Lakes Institute of Management, Gurgaon. Architect by training, building data systems for operations.',
  email: 'siddhantmorye05@gmail.com',
  linkedin: 'https://www.linkedin.com/in/siddhant-morye-67a0761b3/',
  /** Drop an up-to-date PDF at public/resume.pdf and set this to 'resume.pdf' to show the résumé button. */
  resume: null as string | null,
  program: 'PGDM, Analytics & Operations',
  institute: 'Great Lakes Institute of Management, Gurgaon',
  batch: '2025-27',
  prior: 'B.Arch, Pillai College of Architecture',
  basedIn: 'Gurgaon and Navi Mumbai',
};

export type ExperienceEntry = {
  role: string;
  org: string;
  place: string;
  period: string;
  start: string;
  summary: string;
  points: string[];
  workIds?: string[];
};

export const experience: ExperienceEntry[] = [
  {
    role: 'Summer Intern, Analytics & Operations',
    org: 'Ashok Leyland',
    place: 'Alwar Plant 2004, Rajasthan',
    period: 'Apr 2026 - Jun 2026',
    start: '2026',
    summary:
      'Placed in the HR function under the Head of HR. Ran four workstreams that turned manual, paper-bound plant processes into tracked, data-driven systems.',
    points: [
      'Built a QR-based grievance platform in Hindi, English and Marwadi to replace paper Red Books',
      'Engineered a local-LLM Python pipeline over 2,530 vendor files into 1,052,714 clean attendance rows',
      'Traced biometric-to-payroll sync failures to three root causes and a zero-cost staggered schedule',
      'Designed AL-TICS, a CNN tyre-verification system with a PLC line interlock',
    ],
    workIds: ['grievance-platform', 'contractor-absenteeism', 'time-office', 'al-tics'],
  },
  {
    role: 'Architectural Intern',
    org: 'Kembhavi Architecture Foundation',
    place: 'Mumbai',
    period: 'Nov 2022 - May 2023',
    start: '2022',
    summary:
      'Worked on large-scale airport and commercial projects, sitting between design teams, consultants and the client.',
    points: [
      'Ran structured research and gathered stakeholder requirements to support design decisions',
      'Consolidated structural, MEP and landscape inputs into prioritised action trackers',
      'Built client presentation decks with insights, recommendations and next steps, shortening review cycles',
    ],
  },
];

export const education = [
  { degree: 'PGDM, Analytics & Operations', school: 'Great Lakes Institute of Management, Gurgaon', score: 'Pursuing', year: '2027' },
  { degree: 'B.Arch', school: 'Pillai College of Architecture, Navi Mumbai', score: '7.82 / 10', year: '2024' },
  { degree: 'Class XII', school: 'St. Mary’s Junior College, Navi Mumbai', score: '71.38%', year: '2019' },
  { degree: 'Class X', school: 'St. Joseph’s High School, Mumbai', score: '87.00%', year: '2017' },
];

export const awards = [
  { title: '3rd Place, Business Decoded Case Competition', where: 'Great Lakes Institute of Management', year: '2025' },
  { title: 'Finalist, The Quantum Trial analytics case competition', where: 'Inquivista x KOED Learnings, GLIM', year: '2025' },
  { title: '1st Place, 8th Mumbai District Junior Wushu Championship', where: 'Mumbai', year: '2017' },
  { title: '2nd Place, 14th Maharashtra State Junior Wushu Championship', where: 'Maharashtra', year: '2017' },
];

export const positions = [
  { title: 'Member, Harmony (HR Club)', where: 'Great Lakes Institute of Management', year: '2025' },
  { title: 'Graphical-Publication Head', where: 'Pillai College of Architecture', year: '2023' },
  { title: 'Sponsorship & Partnership Lead', where: 'Magazine funding through alumni outreach, brand ads and corporate tie-ups', year: '2023' },
  { title: 'Student Council Member', where: '10+ major events, budget compliance and logistics', year: '2023' },
  { title: 'Volunteer, Talavs of Panvel', where: 'Wetland conservation exhibition with Panvel Municipal Corporation', year: '2022' },
];

export const capabilities = [
  {
    name: 'Analytics',
    items: ['Data pipelines and cleaning at scale', 'Regression, classification, clustering', 'Model explainability (SHAP)', 'Cohort and driver analysis'],
  },
  {
    name: 'Operations',
    items: ['Root-cause analysis', 'Process modelling in BPMN 2.0', 'ERP design and configuration', 'Category and sourcing strategy'],
  },
  {
    name: 'Communication',
    items: ['Dashboards that answer one question each', 'Board-style decks and business plans', 'Stakeholder research', 'Cross-functional coordination'],
  },
];

export const tools = [
  'Python',
  'SQL',
  'Power BI',
  'DAX',
  'Excel',
  'scikit-learn',
  'XGBoost',
  'SHAP',
  'CNNs',
  'Local LLMs',
  'Supabase',
  'Odoo ERP',
  'Bizagi Modeler',
  'Financial modelling',
];

export const groups = {
  internship: { label: 'Internship', plural: 'Internship' },
  competition: { label: 'Case competition', plural: 'Case competitions' },
  academic: { label: 'Academic project', plural: 'Academic projects' },
} as const;
