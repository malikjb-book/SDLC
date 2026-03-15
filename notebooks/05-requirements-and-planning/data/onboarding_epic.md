# Epic: Corporate Entity Resolution Module

## Overview
As part of the GlobalBank Corporate Onboarding platform, we need to completely overhaul how we identify and verify the corporate structures of our applicants to comply with UK FCA Money Laundering / KYC regulations.

## Current State
Today, Risk Analysts and Compliance Officers manually review uploaded PDFs (certificates of incorporation, share registers, partnership agreements). They look for names, search through external government registries (like Companies House), and manually draw org charts in Visio to identify who owns what. It's slow and prone to human error, particularly for multi-layered international holding companies.

## Desired State (The Epic)
The system should allow the client to securely upload their corporate structure documents. An intelligent document processing (IDP) pipeline will extract entities, ownership percentages, and names. The system will cross-reference these names with national business registries to build a verified database graph.

Crucially, the system must automatically trace ownership thresholds up the chain to identify any "Ultimate Beneficial Owner" (UBO) who directly or indirectly controls more than 25% of the entity.

For the Risk Analysts, the system must generate an interactive, visual ownership tree UI so they can see the corporate hierarchy at a glance.

If any entity in the chain is registered in an offshore tax haven (e.g., Cayman Islands, BVI) or a high-risk jurisdiction, the system must automatically flag the overarching onboarding application as "High Risk - Enhanced Due Diligence Required."

## Out of Scope
For this epic, we are NOT integrating adverse media scrape results or PEP screening into the entity resolution module itself (those are distinct Epics). This Epic is purely about unwinding the corporate structure math and visualizing it.
