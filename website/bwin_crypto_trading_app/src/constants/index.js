import {engine, bluecloud, ddb} from "../assets";

export const navLinks = [
  {
    id: "home",
    title: "Home",
  },
  {
    id: "features",
    title: "Features",
  },
  {
    id: "strategies",
    title: "Strategies",
  },
];

export const features = [
  {
    id: "feature-1",
    icon: ddb,
    title: "Data ingestion",
    content:
      "Real-time market data is collected using websockets connected to various exchanges. Price data for many coins are constantly streaming via these websockets and then stored in a database.",
  },
  {
    id: "feature-2",
    icon: engine,
    title: "Execution Engine",
    content:
      "Trading strategies are applied to the market data and orders are sent using APIs provided by exchanges.",
  },
  {
    id: "feature-3",
    icon: bluecloud,
    title: "Distributed Computing",
    content:
      "Services are hosted on GCP, in regions closest to exchanges to optimize for low-latency.",
  },
];

