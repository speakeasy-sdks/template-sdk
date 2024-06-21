/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import { z } from "zod";

/**
 * The type of drink.
 */
export enum DrinkType {
    Cocktail = "cocktail",
    NonAlcoholic = "non-alcoholic",
    Beer = "beer",
    Wine = "wine",
    Spirit = "spirit",
    Other = "other",
}

/** @internal */
export const DrinkType$ = z.nativeEnum(DrinkType);