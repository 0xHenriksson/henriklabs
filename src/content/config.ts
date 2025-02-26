import { z, defineCollection } from 'astro:content';

const nowCollection = defineCollection({
    type: 'content', // v2.5.0 and later
    schema: z.object({
        title: z.string(),
        day: z.string(),
    }),
});

const blogCollection = defineCollection({
    type: 'content', // v2.5.0 and later
    schema: z.object({
        title: z.string(),
        date: z.string(),
        img: z.string().optional(),
        description: z.string().optional(),
        tags: z.array(z.string()).default([]),
    }),
});

export const collections = {
    'now': nowCollection,
    'blog': blogCollection,
};
