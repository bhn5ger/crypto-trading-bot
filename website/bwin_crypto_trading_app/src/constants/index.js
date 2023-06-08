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
      "Before any orders are executed, bWin collects market data using multiple websockets connected to various exchanges. Price data for many coins are constantly streaming via websockets and then stored in an SQL database.",
  },
  {
    id: "feature-2",
    icon: engine,
    title: "Execution Engine",
    content:
      "Using the obtained market data, trading strategies are applied and orders are executed using APIs provided by select exchanges.",
  },
  {
    id: "feature-3",
    icon: bluecloud,
    title: "Distributed Computing",
    content:
      "Services are hosted on GCP, in regions closest to exchanges that are used for trading to optimize for low-latency.",
  },
];

