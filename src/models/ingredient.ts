/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import { IngredientType, IngredientType$ } from "./ingredienttype";
import { z } from "zod";

export type Ingredient = {
    /**
     * The name of the ingredient.
     */
    name: string;
    /**
     * The product code of the ingredient, only available when authenticated.
     */
    productCode?: string | undefined;
    /**
     * The number of units of the ingredient in stock, only available when authenticated.
     */
    stock?: number | undefined;
    /**
     * The type of ingredient.
     */
    type: IngredientType;
};

/** @internal */
export namespace Ingredient$ {
    export type Inbound = {
        name: string;
        productCode?: string | undefined;
        stock?: number | undefined;
        type: IngredientType;
    };

    export const inboundSchema: z.ZodType<Ingredient, z.ZodTypeDef, Inbound> = z
        .object({
            name: z.string(),
            productCode: z.string().optional(),
            stock: z.number().int().optional(),
            type: IngredientType$,
        })
        .transform((v) => {
            return {
                name: v.name,
                ...(v.productCode === undefined ? null : { productCode: v.productCode }),
                ...(v.stock === undefined ? null : { stock: v.stock }),
                type: v.type,
            };
        });

    export type Outbound = {
        name: string;
        productCode?: string | undefined;
        stock?: number | undefined;
        type: IngredientType;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, Ingredient> = z
        .object({
            name: z.string(),
            productCode: z.string().optional(),
            stock: z.number().int().optional(),
            type: IngredientType$,
        })
        .transform((v) => {
            return {
                name: v.name,
                ...(v.productCode === undefined ? null : { productCode: v.productCode }),
                ...(v.stock === undefined ? null : { stock: v.stock }),
                type: v.type,
            };
        });
}
