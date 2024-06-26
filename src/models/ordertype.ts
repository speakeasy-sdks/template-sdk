/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import { z } from "zod";

/**
 * The type of order.
 */
export enum OrderType {
    Drink = "drink",
    Ingredient = "ingredient",
}

/** @internal */
export const OrderType$ = z.nativeEnum(OrderType);
